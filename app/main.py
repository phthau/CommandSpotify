from flask import Flask, request
import logging
import sys
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
from .spotify import SpotifyWrapper
import os
import requests
import base64
import json

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/")
def home_view(): 
    spotify_code = request.args.get('code')
    CLIENT_ID = '<Client>'
    CLIENT_SECRET = '<Secret>'
    CALLBACK_URL = 'http://localhost:5000'
    REDIRECT_URL = 'http://localhost:5000'

    SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"

    auth_token = spotify_code

    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": CALLBACK_URL
    }

    auth = "{}:{}".format(CLIENT_ID, CLIENT_SECRET)
    base64encoded = base64.urlsafe_b64encode(auth.encode('UTF-8')).decode('ascii')
    headers = {"Authorization": "Basic {}".format(base64encoded)}
    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload, headers=headers)
    
    
    if post_request.status_code != 200:
        return 'Error'

    access_token = post_request.json()['access_token']
    
    return access_token

@app.route("/<access>")
def spotify_redirect(access):
    return "The access key I got back is: {}".format(access)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    number = request.form['From']
    message_body = str(request.form['Body']).strip()
    logging.info("Received the following message: {} - {}".format(number, message_body))

    resp = MessagingResponse()
    sp = SpotifyWrapper()

    try:
        if message_body.lower() == "next":
            msg = sp.nextSong()
        elif message_body.lower() == "pause":
            msg = sp.pauseSong()
        elif message_body.lower() == "previous":
            msg = sp.previousSong()
        elif message_body.lower() == "play":
            msg = sp.resumeSong()
        else:
            msg = "Invalid request. Please try next/pause/previous/play."
            logging.info(msg)
    except Exception:
        msg = "An error occurred. Unable to process request."

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