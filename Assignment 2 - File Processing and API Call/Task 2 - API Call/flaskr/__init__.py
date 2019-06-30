import os
from flask import Flask, render_template, jsonify
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

    #Call API and return JSON
    @app.route('/fetch_data_complete')
    def fetch_from_API():
        url = "https://reqres.in/api/users"
        req = requests.get(url)
        data = req.json()
        return jsonify(data)

    # Call API and display the desired data only
    @app.route('/fetch_data_desired')
    def fetch_desired():
        url = "https://reqres.in/api/users"
        req = requests.get(url)
        data = req.json()
        tobedisp = data['data']
        final = []
        for i in tobedisp:
            curr = {}
            curr['id'] = i['id']
            curr['first_name'] = i['first_name']
            curr['last_name'] = i['last_name']
            curr['avatar'] = i['avatar']
            final.append(curr)

        return jsonify(final)

    #Call API and display data in the asked format
    @app.route('/present_data')
    def display_as_desired():
        url = "https://reqres.in/api/users"
        req = requests.get(url)
        data = req.json()
        tobedisp = data['data']

        return render_template('api_output.html',l=tobedisp,n=len(tobedisp))

    return app