from flask import Flask, render_template, jsonify
from datetime import datetime
from datetime import date

import numpy as np

app = Flask(__name__)


def get_retirement():
    retirement = datetime(2027, 2, 26)
    return retirement


def get_countdown():
    now = datetime.now()
    retirement = get_retirement()
    delta = retirement - now

    t = date.today().isoformat()  # e.g. '2026-09-02'
    weekdays = np.busday_count(t, '2027-02-26')

    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return {
        "days": str(days),
        "weekdays": str(weekdays),
        "hours": str(hours),
        "minutes": str(minutes),
        "seconds": str(seconds)
    }

@app.route("/")
def index():
    return render_template("index.html", countdown=get_countdown())


@app.route("/api/countdown")
def api_countdown():
    return jsonify(get_countdown())

if __name__ == "__main__":
    app.run(debug=True)
