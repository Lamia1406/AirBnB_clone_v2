#!/usr/bin/python3
from flask import Flask
"""Flask web application module."""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Route handler for the root URL. returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def only_HBNB():
    """Route handler for the /hbnb URL. returns HBNB!"""
    return "HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def describe_c(text):
    """Route handler for the /c/<text> URL. displays text after c character"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def describe_python(text):
    """Route handler for the /c/<text> URL. displays text after python word"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def display_integer(n):
    """
    Route handler for the /number/<n> URL.
    displays number only if it's integer
    """
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
