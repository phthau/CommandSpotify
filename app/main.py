from flask import Flask, request
import logging
import sys
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/")
def home_view(): 
    return "<h1>Hello World</h1>"

@app.route("/callback", methods=['POST'])
def callback():
    logging.info("Received the following request: {}".format(request.get_json()))
    try:
        return request.get_json()
    except Exception:
        logging.error("Unable to process the request. Received to {}".format(sys.exc_info()[0]))
        return "Unable to process the request."

    return request.get_json()