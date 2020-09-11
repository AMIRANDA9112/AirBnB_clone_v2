#!/usr/bin/python3
"""Flask web application states module"""
from flask import Flask, escape, render_template
from models import storage
from models import State, Amenity, Place

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def display_filters():
    """Return template(states, amenities and cities by state id)"""

    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    places = sorted(storage.all(Place).values(), key=lambda x: x.name)

    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_db(self):
    """close SQLAlchemy Session"""

    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
