#!/usr/bin/python3
"""
a script that starts a Flask web application
The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb: HBnB home page.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Use 8-index.html content as source code for the template 100-hbnb.html:
    Replace the content of the H4 tag under each filter title,
    (H3 States and H3 Amenities) by &nbsp;
    Make sure all HTML tags from objects are correctly used (example:
    <BR /> must generate a new line)
    State, City, Amenity and Place objects must be loaded from DBStorage,
    and sorted by name (A->Z)
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
