import os
from flask import Flask, render_template, request, jsonify
import logging
from elasticsearch import Elasticsearch
from flaskr import db,create_index


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

    #Adding a new product
    @app.route('/product', methods=['POST', 'GET'])
    def add_product():
        if request.method == 'POST':
            prod = {}
            prod['name'] = request.form.get('name')
            prod['price'] = request.form.get('price')
            prod['warranty'] = request.form.get('warranty')
            prod['type'] = request.form.get('type')
            prod['processor'] = request.form.get('processor')
            logging.basicConfig(level=logging.ERROR)
            es = db.connect_elasticsearch()
            to_search = {}
            to_search['query'] = {}
            to_search['size'] = 0
            to_search['query']['match_phrase'] = {}
            to_search['query']['match_phrase']['name'] = prod['name']
            res = es.search(index='catalogue', body=to_search)
            exists = False
            if res['hits']['total']['value']>0:
                exists = True
                res = "This product already exists. Kindly change the Product Name."
            else:
                res = es.index(index="catalogue", doc_type="electronics", id=prod['name'], body=prod)

            return render_template('product_output.html', res=res, prod=prod,exists=exists)

        return render_template('product_form.html')

    # Searching for products
    @app.route('/query', methods=['POST', 'GET'])
    def search_product():
        if request.method == 'POST':
            name = request.form.get('name')
            logging.basicConfig(level=logging.ERROR)
            es = db.connect_elasticsearch()
            to_search = {}
            to_search['query'] = {}
            to_search['query']['match_phrase'] = {}
            to_search['query']['match_phrase']['name'] = name
            res = es.search(index='catalogue', body=to_search)
            print(type(res))
            return render_template('search_output.html', res=res,n=len(res['hits']['hits']))

        return render_template('search_form.html')

    return app