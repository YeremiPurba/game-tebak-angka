import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "kunci-rahasia aplikasi"

# fungsi reset permainan baru
def start_new_game():
    session["secret_number"] = random.randint(1,10)
    session["attempts"] = 5
    session["game_over"] = False
    session["won"] = False
    session["game_started"] = True

# routing new game
@app.route("/new-game", methods=['POST'])
def new_game():
    start_new_game()
    return redirect(url_for("home"))


# routing homepage
@app.route("/")
def home():
    attempts = session.get("attempts", 0)
    game_over = session.get("game_over")
    game_started = session.get("game_started", False)
    return render_template('index.html', attempts=attempts, game_over=game_over, game_started=game_started)

# routing form guess
@app.route("/guess", methods=['POST'])
def guess():
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

    # memeriksa jik kesempatan habis
    if session["attempts"] == 0:
        session["game_over"] = True
        session["won"] = False

    attempts = session["attempts"]
    game_over = session["game_over"]
    game_started = session["game_started"]

    return render_template("index.html", message=message, attempts=attempts, game_over=game_over, game_started=game_started)

if __name__ == "__main__":
    app.run(debug=True)