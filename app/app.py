from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/API")
def do_api_thing():
    url = "https://api.scryfall.com/cards/56ebc372-aabd-4174-a943-c7bf59e5028d"
    reply = requests.get(url).text
    return reply