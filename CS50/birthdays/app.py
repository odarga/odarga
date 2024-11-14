import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/edit", methods=["POST"])
def edit():
        id2 = request.form.get("edit")
        if id2:
            birthdays = db.execute("SELECT * FROM birthdays WHERE id = ?", id2)
            return render_template("edit.html", birthdays=birthdays)
        else:
            month = request.form.get("month_new")
            day = request.form.get("day_new")
            id2 = request.form.get("change")

            if not month or not day:
                return redirect("/")
            else:
                db.execute("UPDATE birthdays SET month = ?, day = ? WHERE id = ?",month, day, id2)
                return redirect("/")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        id1 = request.form.get("delete")
        id2 = request.form.get("edit")

        if id1:
            db.execute("DELETE FROM birthdays WHERE id = ?", id1)
            return redirect("/")

        if not name or not month or not day:
            return redirect("/")
        else:
            db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", name, month, day)
            return redirect("/")

    else:
        birthdays = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays=birthdays)

