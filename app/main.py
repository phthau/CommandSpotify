from flask import Flask, request
import logging
import sys
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse


logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/")
def home_view(): 
    return "<h1>Hello World</h1>"

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    number = request.form['From']
    message_body = str(request.form['Body']).strip()
    logging.info("Received the following message: {} - {}".format(number, message_body))

    resp = MessagingResponse()
    
    if message_body.lower() == "next":
        msg = "Skipping to next song on Spotify!!!!"
    elif message_body.lower() == "pause":
        msg = "Pausing Spotify"
    elif message_body.lower() == "previous":
        msg = "Previous song on Spotify"
    elif message_body.lower() == "play":
        msg = "Resuming Spotify"
    else:
        msg = "Invalid request. Please try next/pause/previous/play."

    logging.info(msg)


    resp = MessagingResponse()
    resp.message(msg)

    # """Respond to incoming calls with a MMS message."""
    # # Start our TwiML response
    # resp = MessagingResponse()

    # # Add a text message
    # msg = resp.message("Test Whats Up! I think you're cute. Gig'em")

    # Add a picture message
    # msg.media("https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg")

    return str(resp)