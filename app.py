from flask import Flask, render_template, jsonify
from datetime import datetime
from datetime import timedelta

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

def get_weekday_countdown():
    now = datetime.now()
    r = get_retirement()
    delta = r - now

    # Count weekdays between now and retirement
    weekdays = 0
    current = now.date()
    end = r.date()
    while current < end:
        if current.weekday() < 5:  # Mon=0 ... Fri=4
            weekdays += 1
        current += timedelta(days=1)

    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return {
        "days": weekdays,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
    }

@app.route("/")
def index():
    return render_template("index.html", countdown=get_countdown(), weekdaycountdown=get_weekday_countdown())


@app.route("/api/countdown")
def api_countdown():
    return jsonify(get_countdown())

@app.route("/api/wdcountdown")
def api_countdown():
    return jsonify(get_weekday_countdown())

if __name__ == "__main__":
    app.run(debug=True)
