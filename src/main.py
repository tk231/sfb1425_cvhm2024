def main():
    from src.update_gspreadsheet import get_date_from_gspreadsheet, connect_to_gspreadsheet
    import src.get_users_and_user_ids_gspreadsheet
    import src.get_user_stats_from_gspreadsheet
    import src.get_user_stats_from_strava

    # Google Sheet details
    google_sheet_key = '1i9D3SBDNKzLrP8ovrKwAuIZlvwCe0HBCPjfhEnHd01A'
    google_sheet_name = 'Sheet1'

    # Init data from Google Sheet
    start_date_cell = 'B1'  # Time is not yet implemented
    end_date_cell = 'E1'
    athlete_name_column = 1
    athlete_id_column = 2
    row_of_start_of_data = 3
    activity_dict = {"Run": 4, "Ride": 6,  # Dictionary containing the activity and the corresponding column number
                     "Walk": 7, "Swim": 9,
                     "Cumulative Elevation": 12,
                     "Cumulative Time": 13,
                     "Number of Activities": 14}

    # Strava details
    strava_client_id = 65701
    strava_client_secret = '60ed605025d846e6c580b66efc997b922cffd819'

    # Connect to the Google Sheet
    worksht = src.update_gspreadsheet.connect_to_googlespreadsheet.connect_to_gspreadsheet(google_sheet_key, google_sheet_name)

    # Get starting date
    start_date = src.update_gspreadsheet.get_date_from_googlespreadsheet.get_epoch_time_from_two_cells_in_googlespreadsheet(worksht,
                                                                                                        start_date_cell)
    end_date = src.update_gspreadsheet.get_date_from_googlespreadsheet.get_epoch_time_from_two_cells_in_googlespreadsheet(worksht, end_date_cell)

    # Create data structures to store activity info
    # user_dict: dictionary from Google Sheets containing all users and their Strava IDs
    # tally_dict: dictionary from Google Sheets containing all the users and their cumulative stats (raw distances,
    # elevation, time and number of activities)
    # update_dict: dictionary containing all the new activities which will be added to tally_dict
    user_dict = src.get_users_and_user_ids_googlespreadsheet.get_users_and_user_ids(worksht,
                                                                                    athlete_name_column,
                                                                                    athlete_id_column,
                                                                                    row_of_start_of_data)

    tally_dict = src.get_user_stats_from_googlespreadsheet.get_user_stats_from_gspreadsheet(worksht,
                                                                                            activity_dict,
                                                                                            athlete_name_column,
                                                                                            row_of_start_of_data)

    # Get user activities from Strava
    update_dict = src.get_user_stats_from_strava.get_user_activities_from_strava()

if __name__ == "__main__":
    main()