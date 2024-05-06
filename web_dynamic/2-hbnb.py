#!/usr/bin/python3

"""
This script starts a Flask web application
It does the following:
- starts a Flask web application
- listens on
- has a route / that displays "Hello HBNB!"
"""

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """
    This removes the current SQLAlchemy Session
    It is triggered when the application context is popped
    If the environment variable HBNB_ENV is equal to test
    It drops all tables
    """
    storage.close()


@app.route('/2-hbnb/', strict_slashes=False)
def hbnb():
    """
    This function renders a template
    It checks if the environment variable HBNB_TYPE_STORAGE is equal to db
    It checks if HBNB_TYPE_STORAGE is equal to file
    It checks if the environment variable HBNB_ENV is equal to test
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """This is the
    Main Function 
    """
    app.run(host='0.0.0.0', port=5001)
