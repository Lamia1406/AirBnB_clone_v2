#!/usr/bin/python3
"""Flask web application module. the module is documented"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_session(error):
    """Remove the current Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states():
    """
    Route handler for the /states_list/ URL.
    displays states list in ul list
    """
    return render_template('7-states_list.html', states=storage.all(State))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
