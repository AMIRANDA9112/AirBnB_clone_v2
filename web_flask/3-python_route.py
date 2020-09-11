#!/usr/bin/python3
"""This module starts a Flask web application"""

from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Return str(Hello HBNB)"""

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Return str(HBNB)"""

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Return str(c + string)"""

    text = escape(text)
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """Return str(Python + string)"""

    text = escape(text)
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
