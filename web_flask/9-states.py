#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """
    display the states and cities listed in alphabetical order
    To load all cities of a State:
    If your storage engine is DBStorage, you must use cities relationship
    Otherwise, use the public getter method cities
    outes:
    /states: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage sorted,
    by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B>
    /states/<id>: display a HTML page: (inside the tag BODY)
    If a State object is found with this id:
    H1 tag: “State: ”
    H3 tag: “Cities:”
    UL tag: with the list of City objects linked to the State sorted,
    by name (A->Z)
    LI tag: description of one City: <city.id>: <B><city.name></B>
    Otherwise:
        H1 tag: “Not found!
    using the option strict_slashes=False in theroute definition
    ”"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


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
