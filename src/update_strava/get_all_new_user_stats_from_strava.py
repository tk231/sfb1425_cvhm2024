def get_all_new_user_stats_from_strava(user_dict, strava_client_id, strava_client_secret, start_datetime, tally_dict):

    from src.update_strava.get_user_stats_from_strava import get_user_activities_from_strava

    print(f"Parsing user activities into spreadsheet")

    for user, user_id in user_dict.items():
        user_activities_df = get_user_activities_from_strava(user_id, strava_client_id, strava_client_secret, start_datetime)

        tally_dict[user]['Run'] = user_activities_df.loc[user_activities_df['type'] == 'Run', 'distance'].sum()
        tally_dict[user]['Ride'] = user_activities_df.loc[user_activities_df['type'] == 'Ride', 'distance'].sum()
        tally_dict[user]['Walk'] = user_activities_df.loc[user_activities_df['type'] == 'Walk', 'distance'].sum()
        tally_dict[user]['Swim'] = user_activities_df.loc[user_activities_df['type'] == 'Swim', 'distance'].sum()
        tally_dict[user]['Cumulative Elevation'] = user_activities_df['total_elevation_gain'].sum()
        tally_dict[user]['Cumulative Time'] = user_activities_df['moving_time'].sum()

    return tally_dict


