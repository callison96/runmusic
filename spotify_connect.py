from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import os
import config

os.environ["SPOTIPY_CLIENT_ID"] = config.SPOTIFY_CLIENT_ID
os.environ["SPOTIPY_CLIENT_SECRET"] = config.SPOTIFY_CLIENT_SECRET

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.current_user_recently_played

tracks = results['items']
while results['next']:
    results = spotify.next(results)
    tracks.extend(results['items'])

for track in tracks:
    print(track['name'])
