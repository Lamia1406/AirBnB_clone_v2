#!/usr/bin/python3
"""Flask web application module."""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_session(error):
    """Remove the current Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_states():
    """
    Route handler for the /states_list/ URL.
    displays states list in ul list
    """
    return render_template('8-cities_by_states.html',
                           states=storage.all(State))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
