#!/usr/bin/python
"""Starts a Flask web application."""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage session."""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def show_cities_by_states():
    """Renders a template with a list of states and their cities."""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
