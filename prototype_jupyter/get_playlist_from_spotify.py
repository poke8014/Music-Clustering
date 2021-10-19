import spotipy
import dotenv
import os
from spotipy.oauth2 import SpotifyOAuth

#import the login files from the .env file
dotenv.load_dotenv(override=True)

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

playlist = sp.playlist_items("4Zqxh2p4XIOZNTI1IiDJvz", 
    fields="items(track(name, href, id, artists))",
    offset=100
    )

# print(playlist)

# get a list of ids for every song

for idx, item in enumerate(playlist['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])


