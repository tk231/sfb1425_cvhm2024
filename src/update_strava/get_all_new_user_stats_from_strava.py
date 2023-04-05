def get_all_user_stats_from_strava(user_dict, strava_client_id, strava_client_secret, start_datetime, end_datetime):
    import time
    from src.update_strava.get_user_stats_from_strava import get_user_activities_from_strava

    print(f"Parsing user activities from Strava")

    # Create dictionary to tally all the parsed (from Strava) numbers
    tally_dict = {}

    for user, user_id in user_dict.items():
        # Get the stats for each user
        tally_dict[user] = {}

        user_activities_df = get_user_activities_from_strava(user_id, strava_client_id, strava_client_secret, start_datetime, end_datetime)

        # Filter user_activities for only interested activities (i.e.: running, cycling, walking, and swimming)
        # Use of '|' instead of 'or' due to need of bitwise operation, else overload
        user_activities_filtered_df = user_activities_df[(user_activities_df['type'] == 'Run') | (user_activities_df['type'] == 'Ride') | (user_activities_df['type'] == 'Walk') | (user_activities_df['type'] == 'Swim')]

        if not user_activities_filtered_df.empty:
            run_sum_in_m = user_activities_filtered_df.loc[user_activities_filtered_df['type'] == 'Run', 'distance'].sum()
            tally_dict[user]['Run'] = run_sum_in_m / 1000
            ride_sum_in_m = user_activities_filtered_df.loc[user_activities_filtered_df['type'] == 'Ride', 'distance'].sum()
            tally_dict[user]['Ride'] = ride_sum_in_m / 1000
            walk_sum_in_m = user_activities_filtered_df.loc[user_activities_filtered_df['type'] == 'Walk', 'distance'].sum()
            tally_dict[user]['Walk'] = walk_sum_in_m / 1000
            swim_sum_in_m = user_activities_filtered_df.loc[user_activities_filtered_df['type'] == 'Swim', 'distance'].sum()
            tally_dict[user]['Swim'] = swim_sum_in_m / 1000
            tally_dict[user]['Cumulative Elevation'] = user_activities_filtered_df['total_elevation_gain'].sum()
            moving_time_in_s = user_activities_filtered_df['moving_time'].sum()
            tally_dict[user]['Cumulative Time'] = time.strftime('%H:%M:%S', time.gmtime(moving_time_in_s))
            tally_dict[user]['Number of Activities'] = user_activities_filtered_df.shape[0]

        else:
            tally_dict[user]['Run'] = 0
            tally_dict[user]['Ride'] = 0
            tally_dict[user]['Walk'] = 0
            tally_dict[user]['Swim'] = 0
            tally_dict[user]['Cumulative Elevation'] = 0
            tally_dict[user]['Cumulative Time'] = 0
            tally_dict[user]['Number of Activities'] = 0

    return tally_dict


