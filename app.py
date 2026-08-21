from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)


def get_retirement():
    now = datetime.now()
    year = now.year
    retirement = datetime(2027, 2, 26)
    return retirement


def get_countdown():
    now = datetime.now()
    christmas = get_retirement()
    delta = christmas - now

    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
    }


@app.route("/")
def index():
    return render_template("index.html", countdown=get_countdown())


@app.route("/api/countdown")
def api_countdown():
    return jsonify(get_countdown())


if __name__ == "__main__":
    app.run(debug=True)
