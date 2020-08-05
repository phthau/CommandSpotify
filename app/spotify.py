import logging

logging.basicConfig(level=logging.INFO)

class SpotifyWrapper:
    def __init__(self):
        # Do all the logic to setup the Spotify API/Config tool here such as API/SDK library configs.
        logging.info("Start of Spotify Wrapper")    
    
    def nextSong(self):
        logging.info("Next...")
        return "Next"

    def previousSong(self):
        logging.info("Previous...")
        return "Previous"
    
    def resumeSong(self):
        logging.info("Resuming...")
        return "Resume"

    def pauseSong(self):
        logging.info("Pausing...")
        return "Pause"


sp = SpotifyWrapper()
sp.previousSong()