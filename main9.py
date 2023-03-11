from flask import Flask, request


# `Flask` is a class we use to instantiate an application
app = Flask(__name__)


# First http GET request
@app.route("/", methods=["GET", "POST"])
def hello_world():

    if request.method == "GET":
        return "<p>GET Hello world!</p>"

    elif request.method == "POST":
        return "<p>POST Hello world!</p>"