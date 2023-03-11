"""
#############################################################################
TOPIC :
1. how to add `templates`?
2. how to pass dynamic values in html page?
#############################################################################
Notes
How to use python expressions and variable names to produce dynamic html page?
for expression in html, tag is  -
    ```
    {% if condition %} .....  {% endif %}
    {% for i in foo %} ..... {% endfor %}
    ```
for variable in html, tag is -
    ```
    {{ variable_name }}
    ```
"""

from flask import Flask, render_template

app = Flask(__name__)


cricketers = ["hardik", "dhoni", "virat"]


@app.route("/cricketers/")   # URL-binding
@app.route("/cricketers/<string:all_>")
def details(all_=None):
    return render_template(
        "dynamic_hello.html",
        all_=all_,
        cricketers=cricketers
    )