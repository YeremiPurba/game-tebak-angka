import random
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, session, redirect, url_for

load_dotenv()
app = Flask(__name__, static_folder="public", static_url_path="")
app.secret_key = os.environ.get("SECRET_KEY")

# fungsi reset permainan baru
def start_new_game(difficulty):
    if difficulty == "easy":
        max_num = 10
        attempts = 5
    elif difficulty == "medium":
        max_num = 50
        attempts = 7
    elif difficulty == "hard":
        max_num = 100
        attempts = 5

    session["max_num"] = max_num
    session["secret_number"] = random.randint(1, max_num)
    session["attempts"] = attempts
    session["game_over"] = False
    session["won"] = False
    session["game_started"] = True

# routing new game
@app.route("/new-game", methods=['POST'])
def new_game():
    difficulty = request.form.get("difficulty")
    start_new_game(difficulty)

    return redirect(url_for("home"))


# routing homepage
@app.route("/")
def home():
    # session.clear()

    max_num = session.get("max_num")
    attempts = session.get("attempts", 0)
    game_over = session.get("game_over")
    game_started = session.get("game_started", False)
    return render_template('index.html', attempts=attempts, game_over=game_over, game_started=game_started, max_num=max_num)

@app.route("/choose-difficulty")
def choose_difficulty():
    session["game_started"] = False
    return redirect(url_for("home"))

# routing form guess
@app.route("/guess", methods=['POST'])
def guess():
    if not session.get("game_started", False):
        return redirect(url_for("home"))

    # mengambil angka tebakan dari user
    guess_number = int(request.form.get("guess_number"))
    # mengambil angka rahasia dari session
    secret_number = session.get("secret_number")

    # logika perbandingan dan pengurangan kesempatan
    if guess_number < secret_number:
        message = "Tebakan terlalu rendah"
        session["attempts"] -= 1
    elif guess_number > secret_number:
        message = "Tebakan terlalu tinggi"
        session["attempts"] -= 1
    else:
        message = "Tebakan benar"
        session["game_over"] = True
        session["won"] = True

    # kesempatan habis
    if session["attempts"] == 0 and not session["won"]:
        message = f"Kamu kalah! Angka rahasianya adalah {secret_number}"
        session["game_over"] = True
        session["won"] = False

    attempts = session["attempts"]
    game_over = session["game_over"]
    game_started = session["game_started"]
    max_num = session.get("max_num")
    won = session.get("won")

    return render_template("index.html", message=message, attempts=attempts, game_over=game_over, game_started=game_started, max_num=max_num, won=won)

if __name__ == "__main__":
    app.run(debug=True)