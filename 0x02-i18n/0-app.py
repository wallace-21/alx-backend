#!/usr/bin/env python3

"""import flask module"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """fucntion that renders a template for a flask app"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
