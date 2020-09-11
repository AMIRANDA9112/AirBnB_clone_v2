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


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Return int(input)"""

    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """Return template(int)"""

    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def slash_number_odd_or_even(n):
    """Return template(int)"""

    value = 'even' if n % 2 == 0 else 'odd'

    return render_template('6-number_odd_or_even.html', n=n, value=value)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
