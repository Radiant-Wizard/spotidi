import os
import argparse as args
from dotenv import load_dotenv
from spotdl import Spotdl
load_dotenv()

client_secret = str(os.getenv("SPOT_CLIENT_SECRET"))
client_id = str(os.getenv("SPOT_CLIENT_ID"))
def cli_down(url : str):
    spotdl = Spotdl(client_secret=client_secret, client_id=client_id)
    songs = spotdl.search([url])
    
    result = spotdl.download_songs(songs)
    song, path = spotdl.download(songs[0])

if  __name__ == "__main__":
    args = args.ArgumentParser("-url", "url of the song")
