#!/usr/bin/python

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def close_storage(exception):
    """
    Close the storage on teardown
    """
    storage.close()

@app.route('/states', defaults={'id': 1}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_states(id):
    """
    Display states by id
    """
    if id == 1:
        states = storage.all(State)
        return render_template('9-states.html', states=states)
    else:
        state = next((state for state in storage.all(State).values() if state.id == id), None)
        return render_template('9-states.html', state=state)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
