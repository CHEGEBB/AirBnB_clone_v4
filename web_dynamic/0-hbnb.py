#!/usr/bin/python3

""" 
This script starts a Flask web application
It does the following:
- starts a Flask web application
- listens on 
- has a route / that displays "Hello HBNB!"
- has a route /hbnb that displays "HBNB"
- has a route /c/<text> that displays "C " followed by the value of the text variable
"""

from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """
    This function closes the database or file storage
    It is triggered when the application context is popped
    When the application stops, the application context is popped
    """
    storage.close()


@app.route('/0-hbnb/', strict_slashes=False)
def hbnb():
    """
    This function renders a template
    It returns the template at web_dynamic/0-hbnb.html
    It passes the following variables to the template:
    - states: a list of State objects
    - amenities: a list of Amenity objects
    - places: a list of Place objects
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
    """
    This block of code is executed if this script is run
    It starts a Flask web application
    """
    app.run(host='0.0.0.0', port=5001)
