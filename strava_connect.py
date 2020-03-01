from stravalib import Client
import config
import datetime

client = Client()

token_response= {
  "access_token": "3d92dca05a0b913a1c0736a04b0387403be6a36d",
  "expires_at": 1583091822,
  "refresh_token": "cc60179727b8100db69184a83a4ed37a675d5e63"}


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
    now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    for activity in client.get_activities(before = now,  limit=1):
        print("{0.name} {0.start_date} {0.elapsed_time}".format(activity))

get_most_recent_activity(client)
