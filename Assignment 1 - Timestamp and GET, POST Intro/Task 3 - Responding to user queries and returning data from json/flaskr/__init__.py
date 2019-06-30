import os
from datetime import datetime
from flask import Flask, request, render_template

import json
with open("flaskr/product.json") as json_file:
    products = json.load(json_file)

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

    #Product query page
    @app.route('/product_query')
    def describe_product():
        query = request.args.get('data')
        present = False
        for i in products:
            if i['product_name'] == query:
                present = True
                target_dict = i
                break
        if present:
            return render_template('product.html', dictionary = target_dict)
        else:
            return render_template('product_unavailable.html')

    # Timestamp returning page
    @app.route('/now')
    def display_timestamp():
        current_dt = datetime.now()
        dt_string = current_dt.strftime("%d-%m-%Y %I:%M %p")
        dt_string = "Hi, current date and time is " + dt_string
        return render_template('timestamp.html',str=dt_string)

    return app