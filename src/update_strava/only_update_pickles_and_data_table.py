def main():
    import yaml
    import datetime
    import os
    import tqdm
    import pandas

    import src.update_strava.load_tokens
    import src.update_strava.get_activity_dataframe

    path_to_strava_yaml = 'resources/strava_app.yaml'
    path_to_strava_tokens = 'resources/athlete_access_tokens'
    path_to_athlete_database = 'data/athlete_database.xlsx'

    # Output paths
    path_to_athlete_pickles = 'data/athlete_pickles'
    path_to_final_table_pickle = 'data/final_table_pickle.pkl'

    # Load strava_app_yaml
    strava_app_deets = yaml.load(open(path_to_strava_yaml), Loader=yaml.Loader)

    end_time = int(datetime.datetime(2024, 6, 26, 23, 23, 59).timestamp())

    # Check for list of athletes
    athlete_db = pandas.read_excel(path_to_athlete_database,
                                   header=None, names=['athlete', 'athlete_id', 'athlete_team'])

    final_table = pandas.DataFrame()

    for athlete_ids in tqdm.tqdm(athlete_db['athlete_id']):
        athlete_name = athlete_db.loc[athlete_db['athlete_id'] == athlete_ids, 'athlete'].item()
        athlete_team = athlete_db.loc[athlete_db['athlete_id'] == athlete_ids, 'athlete_team'].item()
        athlete_json = os.path.join(path_to_strava_tokens, f'strava_token_{athlete_ids}.json')

        path_to_athlete_pickle = os.path.join(path_to_athlete_pickles, f"athlete_{athlete_ids}_pickle.pkl")

        if os.path.exists(path_to_athlete_pickle):
            # Load old pickle
            old_athlete_df = pandas.read_pickle(path_to_athlete_pickle)

            # Get start time from creation time of previous athlete_pickle
            start_time = int(os.path.getmtime(path_to_athlete_pickle))

            # Load and refresh accesss token for athlete
            athlete_token = src.update_strava.load_tokens.load_token(token_path=athlete_json,
                                                                     strava_client_id=strava_app_deets[
                                                                         'strava_client_id'],
                                                                     strava_client_secret=strava_app_deets[
                                                                         'strava_client_secret'])

            # Get new list of activities
            updated_athlete_df = src.update_strava.get_activity_dataframe.get_dataframe_of_activities(
                token=athlete_token,
                start_time=start_time,
                end_time=end_time,
                savepath=None)

            if len(updated_athlete_df) == 0:
                print(f"Athlete {athlete_ids} has 0 new activities")
                athlete_entry_in_final_df = old_athlete_df
            else:
                if len(updated_athlete_df) == 1:
                    print(f"Athlete {athlete_ids} has 1 new activity")
                else:
                    print(f"Athlete {athlete_ids} has {len(updated_athlete_df)} new activities")

                athlete_entry_in_final_df = pandas.concat([old_athlete_df, updated_athlete_df])

            # Save athlete_entry_in_final_df as pickle
            athlete_entry_in_final_df.to_pickle(path_to_athlete_pickle)

            # Prepare athlete entry in final df
            athlete_entry_pickle = pandas.DataFrame()
            athlete_entry_pickle.at[0, 'Athlete'] = athlete_name
            athlete_entry_pickle.at[0, 'Athlete ID'] = int(athlete_ids)
            athlete_entry_pickle.at[0, 'Team'] = int(athlete_team)
            athlete_entry_pickle.at[0, 'Total kilocalories'] = 0

            # Fill in athlete entry pickle
            if len(athlete_entry_in_final_df) == 0:
                pass

            else:
                sport_types: list = athlete_entry_in_final_df['sport_type'].unique()

                # Get distances by activity and fill dataframe with it
                summed_df: pandas.DataFrame = athlete_entry_in_final_df.groupby('sport_type').sum(numeric_only=True)

                for type_of_sport in sport_types:
                    athlete_entry_pickle.at[0, f'{type_of_sport} distance (km)'] = int(
                        summed_df.loc[type_of_sport]['activity_distance'])
                    athlete_entry_pickle.at[0, f'{type_of_sport} moving time'] = datetime.timedelta(
                        seconds=summed_df.loc[type_of_sport]['moving_time'])
                    athlete_entry_pickle.at[0, f'{type_of_sport} elapsed time'] = datetime.timedelta(
                        seconds=summed_df.loc[type_of_sport]['elapsed_time'])
                    athlete_entry_pickle.at[0, f'{type_of_sport} total elevation gain (m)'] = int(
                        summed_df.loc[type_of_sport]['total_elevation_gain'])
                    athlete_entry_pickle.at[0, f'{type_of_sport} kilocalories'] = summed_df.loc[type_of_sport][
                        'kilocalories']
                    athlete_entry_pickle.at[0, 'Total kilocalories'] += summed_df.loc[type_of_sport][
                        'kilocalories']

            # Fill final table
            final_table = pandas.concat([final_table, athlete_entry_pickle], ignore_index=True).fillna(0)

        # Save final table
        final_table.to_pickle(path_to_final_table_pickle)


if __name__ == "__main__":
    main()
