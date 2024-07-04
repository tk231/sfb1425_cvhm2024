import pandas


def get_dataframe_of_activities(token: dict, start_time: int, end_time: int, savepath: str or None) -> pandas.DataFrame:
    """
    Fetch activities from Strava API within a specified time range and return them as a pandas DataFrame.

    Parameters:
    -----------
    token : dict
        Dictionary containing the Strava API access token.
    start_time : int
        Start of the time range for fetching activities.
    end_time : int
        End of the time range for fetching activities.
    savepath : str or None
        Path to save pickle of dataframe if exists, else don't save.

    Returns:
    --------
    pandas.DataFrame
        A DataFrame containing the details of activities between `start_time` and `end_time`.
        Each row represents an activity with columns like 'activity_id', 'activity_name', 'start_date_local',
        'type', 'sport_type', 'activity_distance', 'moving_time', 'elapsed_time', 'total_elevation_gain',
        and 'kilocalories'.

    Description:
    ------------
    This function sends a GET request to the Strava API to retrieve a list of activities within the specified time
    range.
    It creates a DataFrame to store information about each activity. Only non-private activities with a moving time
    greater than 600 seconds are included in the DataFrame.

    If the 'kilojoules' key exists and is not zero, the function calculates kilocalories. Otherwise, it makes an
    additional request to fetch the calories from the activity's detailed information.

    Exceptions:
    -----------
    The function logs an error message if it fails to retrieve the calorie information for an activity.

    Usage:
    ------
    You can use this function to gather Strava activities within a time range and process the data in a DataFrame for
    further analysis.
    """
    import requests

    # Request from API using strava access token
    url = "https://www.strava.com/api/v3/athlete/activities"
    header = {'Authorization': 'Bearer ' + token['access_token']}

    params = {'before': end_time, 'after': start_time, 'per_page': 200}

    r = requests.get(url, headers=header, params=params).json()

    # Create dataframe to save activities
    athlete_df = pandas.DataFrame()

    for activity_num in range(len(r)):
        if r[activity_num]['private']:
            pass
        else:
            activity_moving_time = r[activity_num]['moving_time']
            if activity_moving_time > 600:
                athlete_df.loc[activity_num, "activity_id"] = int(r[activity_num]['id'])
                athlete_df.loc[activity_num, "activity_name"] = r[activity_num]['name']
                athlete_df.loc[activity_num, "start_date_local"] = r[activity_num]['start_date_local']
                athlete_df.loc[activity_num, "sport_type"] = r[activity_num]['sport_type']
                athlete_df.loc[activity_num, "activity_distance"] = r[activity_num]['distance'] / 1000  # Units: km
                athlete_df.loc[activity_num, "moving_time"] = r[activity_num]['moving_time']
                athlete_df.loc[activity_num, "elapsed_time"] = r[activity_num]['elapsed_time']
                athlete_df.loc[activity_num, "total_elevation_gain"] = r[activity_num]['total_elevation_gain']

                activity_id = r[activity_num]['id']
                r_act = requests.get(f"https://www.strava.com/api/v3/activities/{activity_id}/", headers=header,
                                     params={'include_all_efforts': False})

                if r_act.status_code == 200:
                    r_act = r_act.json()
                    athlete_df.loc[activity_num, "kilocalories"] = r_act['calories']
                else:
                    print(
                        f"Unable to get kilocalories for activity {activity_id} from athlete {r[activity_num]['athlete'][id]}"
                    )
                    pass

    if savepath is not None:
        athlete_df.to_pickle(path=savepath)

    return athlete_df
