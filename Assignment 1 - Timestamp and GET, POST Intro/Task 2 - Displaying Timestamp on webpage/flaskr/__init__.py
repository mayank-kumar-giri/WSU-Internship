import os
from datetime import datetime
from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='ACVEADZQRRQW'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Welcome page
    @app.route('/')
    def welcome():
        return "Welcome to the Timestamp Webapp.\n Go to \"http://127.0.0.1:5000/now\" to fetch the current date and time."

    # Timestamp returning page
    @app.route('/now')
    def display_timestamp():
        current_dt = datetime.now()
        dt_string = current_dt.strftime("%d-%m-%Y %I:%M %p")
        dt_string = "Hi, current date and time is " + dt_string + "."
        return dt_string

    return app