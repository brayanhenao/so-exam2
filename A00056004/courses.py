# courses.py
from flask import Flask
import json
app = Flask(__name__)


@app.route("/courses")
def courses():
    courses = {"courses": ["SO2018", "DS2018"]}
    return json.dumps(courses), 200


@app.route("/courses/SO2018/curriculum")
def curriculum():
    curriculum = {"curriculum": ["virtualization", "processes", "memory"]}
    return json.dumps(curriculum), 200


if __name__ == "__main__":
    app.run('0.0.0.0')

