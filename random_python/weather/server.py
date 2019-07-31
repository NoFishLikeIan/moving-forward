from flask import Flask, request
from weather_api import get_forecast
import socket

app = Flask(__name__)


@app.route('/')
def ask_location():
    #location = request.args.get('Location')
    return 'Hello type a location'

@app.route('/<location>')
def weather(location):
    assert isinstance(location, str)
    return get_forecast(location)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
