from flask import Flask, request
import logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/")
def home_view(): 
    return "<h1>Hello World</h1>"

@app.route("/callback", methods=['POST'])
def callback():
    logging.info("Received the following request: {}".format(request.get_json()))
    return request.get_json()