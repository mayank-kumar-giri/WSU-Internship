import os
from datetime import datetime
from flask import Flask, request
import json

with open("flaskr/product.json") as json_file:
    products = json.load(json_file)


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
        return '''<h1><i>Welcome to the Products and Timestamp webpage!</i></h1> <br>
                      <h2>Click below to see examples of product queries:</h2>
                      <ol>
                      <li><a href="http://127.0.0.1:5000/product_query?data=keyboaRd">http://127.0.0.1:5000/product_query?data=keyboaRd</a></li>
                      <li><a href="http://127.0.0.1:5000/product_query?data=laptop">http://127.0.0.1:5000/product_query?data=laptop</a></li>
                      <li><a href="http://127.0.0.1:5000/product_query?data=Projector">http://127.0.0.1:5000/product_query?data=Projector</a></li>
                      <li><a href="http://127.0.0.1:5000/product_query?data=Guitar">http://127.0.0.1:5000/product_query?data=Guitar</a></li>
                      <li><a href="http://127.0.0.1:5000/product_query?data=Presentator">http://127.0.0.1:5000/product_query?data=Presentator</a></li>
                      <li><a href="http://127.0.0.1:5000/product_query?data=Bottles">http://127.0.0.1:5000/product_query?data=Bottles</a></li>
                      </ol>
                      <br>
                      <h2>Click below to see the timestamp:</h2>
                      <h2><a href="http://127.0.0.1:5000/now">http://127.0.0.1:5000/now</a></h2>'''

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
            return '''<h1><u>Product : {}</u></h1>
                      <h2>Supplier : {}</h2>
                      <h2>Quantity : {}</h2>
                      <h2>Unit Cost : {}</h2>
                      <br> <h2><a href="http://127.0.0.1:5000/">Go back to Home Page</a></h2>'''.format(target_dict['product_name'], target_dict['supplier'], target_dict['quantity'], target_dict['unit_cost'])

        else:
            return '''<h1>The product you requested is not present in our database :(</h1> <br> <h2><a href="http://127.0.0.1:5000/">Go back to Home Page</a></h2>'''

    # Timestamp returning page
    @app.route('/now')
    def display_timestamp():
        current_dt = datetime.now()
        dt_string = current_dt.strftime("%d-%m-%Y %I:%M %p")
        dt_string = "Hi, current date and time is " + dt_string
        return '''<h1>{}</h1> <br> <h2><a href="http://127.0.0.1:5000/">Go back to Home Page</a></h2>'''.format(dt_string)

    return app