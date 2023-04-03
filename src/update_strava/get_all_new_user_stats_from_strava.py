def get_all_new_user_stats_from_strava(user_dict, strava_client_id, strava_client_secret, start_datetime, end_datetime):
    import time
    from src.update_strava.get_user_stats_from_strava import get_user_activities_from_strava

    print(f"Parsing user activities into spreadsheet")

    tally_dict = {}

    for user, user_id in user_dict.items():
        user_activities_df = get_user_activities_from_strava(user_id, strava_client_id, strava_client_secret, start_datetime, end_datetime)

        if not user_activities_df.empty:
            run_sum_in_m = user_activities_df.loc[user_activities_df['type'] == 'Run', 'distance'].sum()
            tally_dict[user]['Run'] = run_sum_in_m / 1000
            ride_sum_in_m = user_activities_df.loc[user_activities_df['type'] == 'Ride', 'distance'].sum()
            tally_dict[user]['Ride'] = ride_sum_in_m / 1000
            walk_sum_in_m = user_activities_df.loc[user_activities_df['type'] == 'Walk', 'distance'].sum()
            tally_dict[user]['Walk'] = walk_sum_in_m / 1000
            swim_sum_in_m = user_activities_df.loc[user_activities_df['type'] == 'Swim', 'distance'].sum()
            tally_dict[user]['Swim'] = swim_sum_in_m / 1000
            tally_dict[user]['Cumulative Elevation'] = user_activities_df['total_elevation_gain'].sum()
            moving_time_in_s = user_activities_df['moving_time'].sum()
            tally_dict[user]['Cumulative Time'] = time.strftime('%H:%M:%S', time.gmtime(moving_time_in_s))
            tally_dict[user]['Number of Activities'] = user_activities_df.shape[0]

        else:
            tally_dict[user]['Run'] = 0
            tally_dict[user]['Ride'] = 0
            tally_dict[user]['Walk'] = 0
            tally_dict[user]['Swim'] = 0
            tally_dict[user]['Cumulative Elevation'] = 0
            tally_dict[user]['Cumulative Time'] = 0
            tally_dict[user]['Number of Activities'] = 0

    return tally_dict


