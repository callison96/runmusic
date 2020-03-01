from stravaio import strava_oauth2
import time
import swagger_client
from swagger_client.rest import ApiException
import config

#access_token = strava_oauth2(client_id=config.STRAVA_CLIENT_ID,
        #        client_secret=config.STRAVA_CLIENT_SECRET)

swagger_client.configuration.access_token = config.STRAVA_TOKEN

api_instance = swagger_client.ActivitiesApi()
before = 56 # Integer | An epoch timestamp to use for filtering activities that have taken place before a certain time. (optional)
after = 56 # Integer | An epoch timestamp to use for filtering activities that have taken place after a certain time. (optional)
page = 56 # Integer | Page number. (optional)
perPage = 30 # Integer | Number of items per page. Defaults to 30. (optional) (default to 30)

try:
    # List Athlete Activities
    api_response = api_instance.getLoggedInAthleteActivities(before=before, after=after, page=page, perPage=perPage)
    print(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->getLoggedInAthleteActivities: %s\n" % e)
