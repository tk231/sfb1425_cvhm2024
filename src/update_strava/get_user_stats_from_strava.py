def get_user_activities_from_strava(athlete_id, strava_client_id, strava_client_secret, start_datetime, end_datetime):
    """
    Gets activities from single user off Strava

    :param athlete_id:
    :param strava_client_id:
    :param strava_client_secret:
    :param start_datetime:
    :param end_datetime:
    :return:
    """
    import json
    import time
    import requests
    import pandas as pd

    strava_api_url = "https://www.strava.com/api/v3/activities"

    path_to_jsons = '/mnt/Aruba/PyCharmProjects/strava_club_challenge_automated/logins/strava'

    # Open json file to connect to Strava
    with open(f'{path_to_jsons}/strava_token_{athlete_id}.json') as json_file:
        strava_token = json.load(json_file)

    # If access_token has expired, use refresh_token to get new access_token
    if strava_token['expires_at'] < time.time():
        # Make new request
        response = requests.post(
            url='https://www.strava.com/oauth/token',
            data={
                'client_id': strava_client_id,
                'client_secret': strava_client_secret,
                'grant_type': 'refresh_token',
                'refresh_token': strava_token['refresh_token']
            }
        )

        # Save response as json in new variable
        new_strava_token = response.json()

        # Save new tokens to file
        with open(f'{path_to_jsons}/strava_token_{athlete_id}.json', 'w') as outfile:
            json.dump(new_strava_token, outfile)

        # Use new Strava tokens from now onwards
        strava_token = new_strava_token

    # Get page of activities from Strava
    number_of_activities_to_parse = 300
    r = requests.get \
        (f"{strava_api_url}?access_token={strava_token['access_token']}&per_page={number_of_activities_to_parse}&page=1")

    # If OK status received
    if r.status_code == 200:
        r = r.json()
        user_activities_df = pd.DataFrame(columns=["id",
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

        # if r['message'] == 'Authorization Error':
        #     continue

        for x in range(len(r)):
            # Skip if activity is private
            if r[x]['private'] is True:
                pass
            else:
                # Check if moving time is at least half of the elapsed time
                moving_time = r[x]['moving_time']
                elapsed_time = r[x]['elapsed_time']
                start_date_local = r[x]['start_date_local']
                if (moving_time <= elapsed_time) and (moving_time >= (0.5 * elapsed_time)) and \
                        (start_datetime <= start_date_local < end_datetime):
                    user_activities_df.loc[x, 'id'] = r[x]['id']
                    user_activities_df.loc[x, 'name'] = r[x]['name']
                    user_activities_df.loc[x, 'start_date_local'] = r[x]['start_date_local']
                    user_activities_df.loc[x, 'type'] = r[x]['type']
                    user_activities_df.loc[x, 'distance'] = r[x]['distance']
                    user_activities_df.loc[x, 'moving_time'] = r[x]['moving_time']
                    user_activities_df.loc[x, 'elapsed_time'] = r[x]['elapsed_time']
                    user_activities_df.loc[x, 'total_elevation_gain'] = r[x]['total_elevation_gain']

        # Check if user_activities_df are nearing the number_of_activities_to_parse limit
        number_of_activities_in_user_activities_df = user_activities_df.shape[0]
        if number_of_activities_in_user_activities_df + 20 > number_of_activities_to_parse:
            print(f"Athlete {athlete_id}'s user_activities_df length has {number_of_activities_in_user_activities_df}, "
                  f"time to increase number_of_activities_to_parse!")

        return user_activities_df

    else:
        print(f"Problem with athlete {athlete_id}!")
