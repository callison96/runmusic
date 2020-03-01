import sys
import spotipy
import spotipy.util as util
import config
import os

def spotify_auth(username):

    os.environ["SPOTIPY_CLIENT_ID"] = config.SPOTIFY_CLIENT_ID
    os.environ["SPOTIPY_CLIENT_SECRET"] = config.SPOTIFY_CLIENT_SECRET
    os.environ["SPOTIPY_REDIRECT_URI"] = config.SPOTIFY_REDIRECT_URI

    scope = 'user-read-recently-played'

    token = util.prompt_for_user_token(username, scope)
    return token

def get_latest_tracks(username, before, after, limit):

    token = spotify_auth(username)


    if token:
        sp = spotipy.Spotify(auth=token)
        results_before = sp.current_user_recently_played(limit=limit, before= int(before))
        track_list_before = []
        track_list_after = []
        for item in results_before['items']:
            print (item['played_at'])
            print (get_track_duration(username,item['track']['id']))
            print ()
            track = item['track']
            track_list_before.append(track['name'] + ' - ' + track['artists'][0]['name'])


        results_after =  sp.current_user_recently_played(limit = limit, after= int(after))
        for item in results_after['items']:
            track = item['track']
            track_list_after.append(track['name'] + ' - ' + track['artists'][0]['name'])


        return track_list_before, track_list_after
    else:
        print("Can't get token for", username)

def get_track_duration(username, id):
    token = spotify_auth(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.track(id)
        print (results['duration_ms'])
