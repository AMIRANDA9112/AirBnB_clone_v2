#!/usr/bin/python3
"""Flask web application states module"""
from flask import Flask, escape, render_template
from models import storage
from models import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    """Return states"""

    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(self):
    """close SQLAlchemy Session"""

    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
