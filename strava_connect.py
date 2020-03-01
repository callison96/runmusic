from stravalib import Client
import config
import datetime
import pytz
from spotify_auth import get_latest_tracks

client = Client()

token_response= {
  "access_token": "87f0a2299c12e6b5b22fe3b67e8dc003d014f728",
  "expires_at": 1583098922,
  "refresh_token": "587e4d536796c0935a37a93d5b537c56720c74f0"
}


access_token = token_response['access_token']
refresh_token = token_response['refresh_token']
expires_at = token_response['expires_at']

# Now store that short-lived access token somewhere (a database?)
client.access_token = access_token
# You must also store the refresh token to be used later on to obtain another valid access token
# in case the current is already expired
client.refresh_token = refresh_token

# An access_token is only valid for 6 hours, store expires_at somewhere and
# check it before making an API call.
client.token_expires_at = expires_at

athlete = client.get_athlete()
print("For {id}, I now have an access token {token}".format(id=athlete.firstname, token=access_token))

def get_most_recent_activity(client):
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    now = utc_now.strftime("%Y-%m-%dT%H:%M:%SZ")
    for activity in client.get_activities(before=now, limit=1):
        #already returned in utc
        return activity


def get_activity_length(activity):
    return [activity.start_date, activity.start_date + activity.elapsed_time]


recent_activity = get_most_recent_activity(client)

activity_start_end = get_activity_length(recent_activity)

test_time_before =  pytz.utc.localize(datetime.datetime.utcnow())

test_time_after = test_time_before - datetime.timedelta(hours=1)

#track_list = get_latest_tracks(config.SPOTIFY_USERNAME,
#                    before = activity_start_end[1].timestamp()*1000,
#                    limit = 5)

results_before, results_after = get_latest_tracks(config.SPOTIFY_USERNAME,
                    before = test_time_before.timestamp()*1000,
                    after = test_time_after.timestamp()*1000,
                    limit = 25)

print (set(results_before) & set(results_after))

#client.update_activity(recent_activity.id, description = str(track_list))
#print ('Updated description:' , str(track_list))
