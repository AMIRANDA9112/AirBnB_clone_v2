#!/usr/bin/python3
"""Flask web application states module"""
from flask import Flask, escape, render_template
from models import storage
from models import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_states_cities(id=None):
    """Return state by id """

    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    selected_state = None
    if id:
        for state in states:
            if state.id == id:
                selected_state = state

    return render_template('9-states.html', states=states,
                           id=id, selected_state=selected_state,)


@app.teardown_appcontext
def teardown_db(self):
    """close SQLAlchemy Session"""

    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
