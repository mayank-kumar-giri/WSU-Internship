import os
from flask import Flask, render_template, jsonify, request
import requests


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Welcome page
    @app.route('/')
    def welcome():
        return render_template('index.html')

    # Call API and return weather report
    @app.route('/chatbot', methods=['POST', 'GET'])
    def conversation():
        if request.method == 'POST':
            question = request.form.get('question')


            return

        return render_template('weather_form.html')

    return app