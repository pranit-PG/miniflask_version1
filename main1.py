"""
Hello world application of Flask
Command - `flask --app main run`
- HOME URL
https://swapi.dev
http://127.0.0.1:5000
- RELATIVE
/api/films
- ABSOLUTE URL
"""

from flask import Flask


# `Flask` is a class we use to instantiate an application
app = Flask(__name__)


# First http GET request
@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"


# SECOND http GET request
@app.route("/greeting")
def custom_message():

    import requests

    response = requests.get("https://swapi.dev/api/films/1")
    # store response in DB
    return "<h1>data has been saved in DB</h1"

# h1 is used to highlight(bold) the text.
# h2 makes littlebit less bold