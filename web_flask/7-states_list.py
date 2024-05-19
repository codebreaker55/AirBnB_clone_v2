#!/usr/bin/python3
"""
a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    a HTML page with the states listed in alphabetical order
    Routes:
    /states_list: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage sorted,
    by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B>display,
    """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
