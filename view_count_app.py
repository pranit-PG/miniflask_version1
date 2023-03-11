"""
REST APIs need to be stateless
"""

from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to this flash card application!!!"


@app.route("/date")
def date():
    return f"This page was served at - {str(datetime.now())}"


counter = 0


@app.route("/refresh_count")
def count():
    global counter
    counter += 1
    return f"This page was visited {counter} times"