import sys
import spotipy
import spotipy.util as util
import config
import os

def get_latest_tracks(username, before, limit):

    os.environ["SPOTIPY_CLIENT_ID"] = config.SPOTIFY_CLIENT_ID
    os.environ["SPOTIPY_CLIENT_SECRET"] = config.SPOTIFY_CLIENT_SECRET
    os.environ["SPOTIPY_REDIRECT_URI"] = config.SPOTIFY_REDIRECT_URI

    scope = 'user-read-recently-played'

    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_recently_played(limit=limit, before= int(before))
        track_list = []
        for item in results['items']:
            track = item['track']
            track_list.append(track['name'] + ' - ' + track['artists'][0]['name'])

        return track_list
    else:
        print("Can't get token for", username)
