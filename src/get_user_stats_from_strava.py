import pandas as pd


def get_user_activities_from_strava(athlete_id, last_update_epoch, strava_client_id, strava_client_secret):
    import json
    import time
    import requests

    strava_api_url = "https://www.strava.com/api/v3/activities"

    # Open json file to connect to Strava
    with open(f'strava_tokens_{athlete_id}.json') as json_file:
        strava_tokens = json.load(json_file)

    # If access_token has expired, use refresh_token to get new access_token
    if strava_tokens['expires_at'] < time.time():
        # Make new request
        response = requests.post(
            url='https://www.strava.com/oauth/token',
            data={
                'client_id': strava_client_id,
                'client_secret': strava_client_secret,
                'grant_type': 'refresh_token',
                'refresh_token': strava_tokens['refresh_token']
            }
        )

        # Save response as json in new variable
        new_strava_tokens = response.json()

        # Save new tokens to file
        with open('strava_tokens.json', 'w') as outfile:
            json.dump(new_strava_tokens, outfile)

        # Use new Strava tokens from now onwards
        strava_tokens = new_strava_tokens

    # Get page of activities from Strava
    r = requests.get(f"{strava_api_url}?access_token={strava_tokens['access_token']}&per_page=20&page=1")
    r = r.json()

    user_activites = pd.DataFrame(columns=["id",
                                           "name",
                                           "start_date_local",
                                           "type",
                                           "distance",
                                           "moving_time",
                                           "elapse_time",
                                           "total_elevation_gain",
                                           "private"
                                           ]
                                  )

    for x in range(len(r)):
        user_activites.loc[x, 'id'] = r[x]['id']
        user_activites.loc[x, 'name'] = r[x]['name']
        user_activites.loc[x, 'start_date_local'] = r[x]['start_date_local']
        user_activites.loc[x, 'type'] = r[x]['type']
        user_activites.loc[x, 'distance'] = r[x]['distance']
        user_activites.loc[x, 'moving_time'] = r[x]['moving_time']
        user_activites.loc[x, 'elapse_time'] = r[x]['elapse_time']
        user_activites.loc[x, 'total_elevation_gain'] = r[x]['total_elevation_gain']
        user_activites.loc[x, 'private'] = r[x]['private']

    return user_activites
