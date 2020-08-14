from flask import Flask, request, abort, Response, redirect
import os
import requests
import base64
import json
import logging
import sys
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
from .spotify import SpotifyWrapper
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

    
CLIENT_ID = "<CLIENT_ID>"
CLIENT_SECRET = "<CLIENT_SECRET"
CALLBACK_URL = "<CALLBACK_URL"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
    
##TODO: refreshtoken
@app.route("/")
def home():
    auth_token = request.args.get('code')
    data = {
        'grant_type': "authorization_code", 
        'code': str(auth_token),
        'redirect_uri': CALLBACK_URL
    }
    auth = "{}:{}".format(CLIENT_ID, CLIENT_SECRET)
    base64encoded = base64.urlsafe_b64encode(auth.encode('UTF-8')).decode('ascii')
    headers = {"Authorization": "Basic {}".format(base64encoded)}
    post_request = requests.post(url = SPOTIFY_TOKEN_URL, data = data, headers = headers)
    
    re = json.loads(post_request.content)
    return re

@app.route("/sms/", methods=['GET', 'POST'])
def sms_reply():
    message_body = str(request.form['Body']).strip()
    number = request.form['From']
    logging.info("Received the following message: {} - {}".format(number, message_body))

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
    return str(resp)