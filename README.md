# runmusic
Update Strava activities with Spotify track information

## Initial Testing
You will need to use oauth2 to set up and test with your spotify account.
The easiest way I have found to do this is to use the example from the stravalib
python library <https://github.com/hozn/stravalib/tree/master/examples/strava-oauth>.

If you run this flask app then you can get the access_token to input into strava_connect.py.
You may want to change the scope in server.py/authorization_url to something like:

```python
scope = ['read','activity:read','profile:write']
```

This will give you access to change values. 
