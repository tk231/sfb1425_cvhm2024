import pandas as pd


def get_user_activities_from_strava(athlete_id, strava_client_id, strava_client_secret, start_datetime,
                                    cutoff_datetime):
    import json
    import time
    import requests

    strava_api_url = "https://www.strava.com/api/v3/activities"

    path_to_jsons = '/mnt/Aruba/PyCharmProjects/strava_club_challenge_automated/logins/strava'

    # Open json file to connect to Strava
    with open(f'{path_to_jsons}/strava_token_{athlete_id}.json') as json_file:
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
        new_strava_token = response.json()

        # Save new tokens to file
        with open('strava_tokens.json', 'w') as outfile:
            json.dump(new_strava_token, outfile)

        # Use new Strava tokens from now onwards
        strava_token = new_strava_token

    # Get page of activities from Strava
    r = requests.get(f"{strava_api_url}?access_token={strava_tokens['access_token']}&per_page=20&page=1")
    r = r.json()

    user_activities = pd.DataFrame(columns=["id",
                                            "name",
                                            "start_date_local",
                                            "type",
                                            "distance",
                                            "moving_time",
                                            "elapsed_time",
                                            "total_elevation_gain",
                                            "private"
                                            ]
                                   )

    for x in range(len(r)):
        user_activities.loc[x, 'id'] = r[x]['id']
        user_activities.loc[x, 'name'] = r[x]['name']
        user_activities.loc[x, 'start_date_local'] = r[x]['start_date_local']
        user_activities.loc[x, 'type'] = r[x]['type']
        user_activities.loc[x, 'distance'] = r[x]['distance']
        user_activities.loc[x, 'moving_time'] = r[x]['moving_time']
        user_activities.loc[x, 'elapsed_time'] = r[x]['elapsed_time']
        user_activities.loc[x, 'total_elevation_gain'] = r[x]['total_elevation_gain']
        user_activities.loc[x, 'private'] = r[x]['private']

    last_activity_time = user_activities.iloc[0]['start_date_local']
    filtered_user_activities_df = user_activities[
        user_activities['start_date_local'] > start_datetime & user_activities['start_date_local'] <= cutoff_datetime]

    return filtered_user_activities_df
