"""
QUERY params

"""

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


################################################
# how to access PATH parameter in Flask?      #
################################################
@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f"subpath - {subpath}"


################################################
# how to access query parameter in Flask?      #
################################################
@app.route("/about")
def about():
    institute = request.args.get("institute")
    return f"<p>{institute}</p>"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)