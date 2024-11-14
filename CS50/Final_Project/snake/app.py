from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///snake.db")

@app.route("/")
def index():

    session.clear()
    highscores = db.execute("SELECT * FROM classic ORDER BY score DESC LIMIT 3")
    multihighscores = db.execute("SELECT * FROM multi ORDER BY score DESC LIMIT 3")

    return render_template("index.html", highscores=highscores, multihighscores=multihighscores)

@app.route("/classic", methods = ["GET", "POST"])
def classic():

    if(request.method == "POST"):

        player1 = request.form.get("player1")
        session["player1"] = player1
        return render_template("gameclassic.html", player1=player1)

    else:
        return render_template("classic.html")

@app.route("/multi", methods = ["GET", "POST"])
def multi():

    if(request.method == "POST"):

        player1 = request.form.get("player1")
        player2 = request.form.get("player2")
        session["player1"] = player1
        session["player2"] = player2

        return render_template("gamemulti.html", player1=player1, player2=player2)

    else:

        return render_template("multi.html")

@app.route("/gameclassic", methods = ["GET", "POST"])
def gameclassic():

    if(request.method == "POST"):
        score = request.data
        decoded_score = score.decode("utf-8")
        db.execute("INSERT INTO classic (username, score) VALUES (?, ?)", session["player1"], decoded_score)

        return render_template("gameclassic.html")

    else:
        return render_template("gameclassic.html")

@app.route("/gamemulti", methods = ["GET", "POST"])
def gamemulti():

    if(request.method == "POST"):
        score = request.data
        decoded_score = score.decode("utf-8")
        score_list = decoded_score.split(",")
        db.execute("INSERT INTO multi (username, score) VALUES (?, ?)", session["player1"], score_list[0])
        db.execute("INSERT INTO multi (username, score) VALUES (?, ?)", session["player2"], score_list[1])

        return render_template("gamemulti.html")

    else:
        return render_template("gamemulti.html")
