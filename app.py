from flask import Flask, render_template, request

app = Flask(__name__)

REGISTRANTS = {}
SPORT = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]

@app.route("/")
def index():
    return render_template("index.html", sports = SPORT)

@app.route("/register", methods = ["POST", "GET"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name:
        return render_template("failure.html")
    if sport not in SPORT:
        return render_template("failure.html")
    REGISTRANTS[name] = sport
    return render_template("success.html")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants = REGISTRANTS)

if __name__ == '__main__':
    app.run(debug=True)
