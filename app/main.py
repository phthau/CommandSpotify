from flask import Flask, request
import logging
import sys
from twilio.twiml.messaging_response import MessagingResponse

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


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a MMS message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a text message
    msg = resp.message("The Robots are coming! Head for the hills!")

    # Add a picture message
    msg.media("https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg")

    return str(resp)