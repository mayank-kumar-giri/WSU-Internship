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

    #Call API and return weather report
    @app.route('/weather', methods=['POST', 'GET'])
    def fetch_weather():
        if request.method == 'POST':
            zipcode = request.form.get('zipcode')
            url1 = "http://api.openweathermap.org/data/2.5/weather?q="
            suffix = "&APPID="
            API_KEY = "133066a3b21013516c0d275a45ad4223"
            weather_url = url1 + zipcode + suffix + API_KEY
            url2 = "http://api.zippopotam.us/us/"
            location_url = url2 + zipcode
            req = requests.get(weather_url)
            weather = req.json()
            req = requests.get(location_url)
            location = req.json()
            if location=={}:
                state = ""
                sabv = ""
            else:
                state = location["places"][0]["state"]
                sabv = location["places"][0]["state abbreviation"]

            if weather["cod"] == 200:
                valid=True
                weather["main"]["temp"] = round(weather["main"]["temp"] - 273.15, 4)
            else:
                valid=False

            return render_template('weather_output.html', data=weather, valid=valid,s=state,sa=sabv)

        return render_template('weather_form.html')

    return app