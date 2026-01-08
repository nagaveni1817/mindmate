from flask import Flask, render_template, request

app = Flask(__name__)

# Simple joke list (SF-safe)
JOKES = [
    "Why did the student bring a ladder to class? Because they were going to the next level 😄",
    "Your brain isn’t tired — it’s just buffering for a moment 🙂"
]

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/checkin")
def checkin():
    return render_template("checkin.html")

@app.route("/decision", methods=["POST"])
def decision():
    stress = request.form.get("stress")

    if stress == "Low":
        state = "STABLE"
    elif stress == "Medium":
        state = "FOCUS_LOSS"
    else:
        state = "OVERLOAD"

    return render_template("decision.html", state=state)

@app.route("/humor")
def humor():
    # First joke
    return render_template("humor.html", joke=JOKES[0], step=1)

@app.route("/humor_response", methods=["POST"])
def humor_response():
    response = request.form.get("response")
    step = int(request.form.get("step"))

    if response == "yes":
        return render_template("after_humor.html")

    if step == 1:
        # Show second joke
        return render_template("humor.html", joke=JOKES[1], step=2)

    # If still stressed after second joke → move to calm
    return render_template("calm.html")
@app.route("/focus")
def focus():
    return render_template("focus.html")

@app.route("/motivation")
def motivation():
    return render_template("motivation.html")


if __name__ == "__main__":
    app.run(debug=True)
