import logging
import requests
import os
import base64
import json

logging.basicConfig(level=logging.INFO)


class SpotifyWrapper:
    def __init__(self, access_token):
        logging.info("Start of Spotify Wrapper")
        self.access_token = access_token
        logging.info("Done setting up!!!")

    def nextSong(self):
        logging.info("Next...")
        NEXT_URL = "https://api.spotify.com/v1/me/player/next"
        headers = {"Authorization": "Bearer {}".format(self.access_token)}
        requests.post(url=NEXT_URL, headers=headers)
        return "Next"

    def previousSong(self):
        logging.info("Previous...")
        PREV_URL = "https://api.spotify.com/v1/me/player/previous"
        headers = {"Authorization": "Bearer {}".format(self.access_token)}
        requests.post(url=PREV_URL, headers=headers)
        return "Previous"

    def resumeSong(self):
        logging.info("Resuming...")
        RESUME_URL = "https://api.spotify.com/v1/me/player/play"
        headers = {"Authorization": "Bearer {}".format(self.access_token)}
        r = requests.put(url=RESUME_URL, headers=headers)
        logging.info(r.text)
        return "Resume"

    def pauseSong(self):
        logging.info("Pausing...")
        PAUSE_URL = "https://api.spotify.com/v1/me/player/pause"
        headers = {"Authorization": "Bearer {}".format(self.access_token)}
        requests.put(url=PAUSE_URL, headers=headers)
        return "Pause"
