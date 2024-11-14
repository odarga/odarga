import os
import datetime
import pytz

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    stocks = db.execute("SELECT stockname, SUM(shares) as shares FROM stocks WHERE username = ? GROUP BY stockname", user[0]["username"])
    cash = usd(float(user[0]["cash"]))
    x = len(stocks)
    total = 0
    for i in range(x):
        stockname = stocks[i]['stockname']
        stockinfo = lookup(stockname)
        stockprice = stockinfo['price']
        stocks[i]['price'] = float(stockprice)
        stocks[i]['total'] = float(stocks[i]['price'] * stocks[i]['shares'])
        total += float(stocks[i]['total'])

    grandtotal = float(user[0]["cash"]) + float(total)
    total = usd(total)
    grandtotal = usd(grandtotal)
    return render_template("index.html",grandtotal=grandtotal, total=total, cash=cash, stocks=stocks)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():

    if request.method == "POST":
        """Buy shares of stock"""
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("must provide stock", 403)

        if not shares.isdigit() or int(shares) == 0:
            return apology("must provide positive number of shares", 403)

        stocks = lookup(symbol)

        if stocks == None :
            return apology("stock does not exist", 403)

        name = stocks['name']
        value = stocks['price']
        total_value = value * float(shares)
        user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        time = datetime.datetime.now(pytz.timezone("US/Eastern"))
        date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
        if total_value > float(user[0]["cash"]):
            return apology("not enough balance", 403)
        else:
            db.execute("UPDATE users SET cash = ? WHERE id = ?",float(user[0]["cash"]) - total_value, session["user_id"])
            user_stocks = db.execute("SELECT stockname FROM stocks WHERE username = ?", user[0]["username"])
            db.execute("INSERT INTO stocks (username, stockname, shares) VALUES (?, ?, ?)", user[0]["username"], name, int(shares))
            db.execute("INSERT INTO actions (username, stockname, shares, price, action, date) VALUES (?, ?, ?, ?, ?, ?)", user[0]["username"], name, int(shares), value, "buy", date_time)
            return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    actions = db.execute("SELECT * FROM actions WHERE username = ?", user[0]["username"])
    return render_template("history.html", actions=actions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():

    if request.method == "POST":
        """Get stock quote."""
        symbol = request.form.get("symbol")
        stocks = lookup(symbol)

        if stocks == None :
            return apology("stock does not exist", 403)

        name = stocks['name']
        value = usd(stocks['price'])
        return render_template("quoted.html", name=name, value=value)
    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        """Register user"""
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        users = db.execute("SELECT username FROM users")
        if not username:
            return apology("must provide username", 403)

        if username in users:
            return apology("username already exists", 403)

        if not password:
            return apology("must provide password", 403)

        if password != confirmation:
            return apology("passwords do not match", 403)

        hash = generate_password_hash(password)

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():

    if request.method == "POST":
        """Sell shares of stock"""
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("must provide stock", 403)

        if not shares.isdigit() or int(shares) == 0:
            return apology("must provide positive number of shares", 403)

        user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        stocks = db.execute("SELECT stockname, SUM(shares) as shares FROM stocks WHERE username = ? GROUP BY stockname", user[0]["username"])
        x = len(stocks)
        for i in range(x):
            if symbol == stocks[i]['stockname'] and int(shares) > stocks[i]['shares']:
                return apology("not enouth shares", 403)

        stocks = lookup(symbol)
        name = stocks['name']
        value = stocks['price']
        total_value = value * float(shares)
        time = datetime.datetime.now(pytz.timezone("US/Eastern"))
        date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
        db.execute("UPDATE users SET cash = ? WHERE id = ?",float(user[0]["cash"]) + total_value, session["user_id"])
        db.execute("INSERT INTO stocks (username, stockname, shares) VALUES (?, ?, ?)", user[0]["username"], name, -int(shares))
        db.execute("INSERT INTO actions (username, stockname, shares, price, action, date) VALUES (?, ?, ?, ?, ?, ?)", user[0]["username"], name, int(shares), value, "sell", date_time)
        return redirect("/")

    else:
        user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        stocks = db.execute("SELECT stockname, SUM(shares) as shares FROM stocks WHERE username = ? GROUP BY stockname", user[0]["username"])
        return render_template("sell.html", stocks=stocks)


@app.route("/password", methods=["GET", "POST"])
@login_required
def password():

    if request.method == "POST":
        """Change password"""
        old_password = request.form.get("oldpassword")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not old_password:
            return apology("must provide old password", 403)

        if not password:
            return apology("must provide new password", 403)

        if password != confirmation:
            return apology("passwords do not match", 403)

        user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        # Ensure username exists and password is correct
        if not check_password_hash(user[0]["hash"], old_password):
            return apology("invalid old password", 403)

        hash = generate_password_hash(password)

        db.execute("UPDATE users SET hash = ? WHERE username = ?", hash, user[0]["username"])
        return redirect("/")

    else:
        return render_template("password.html")
