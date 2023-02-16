def get_all_new_user_stats_from_strava(user_dict, strava_client_id, strava_client_secret, start_datetime, tally_dict):
    import time
    from src.update_strava.get_user_stats_from_strava import get_user_activities_from_strava

    print(f"Parsing user activities into spreadsheet")

    for user, user_id in user_dict.items():
        user_activities_df = get_user_activities_from_strava(user_id, strava_client_id, strava_client_secret, start_datetime)

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

    return tally_dict


