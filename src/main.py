def main():
    import src
    from src.update_gspreadsheet import get_date_from_gspreadsheet, connect_to_gspreadsheet, \
        get_users_and_user_ids_gspreadsheet, get_current_stats_from_gspreadsheet, update_gspreadsheet_with_strava_data
    from src.update_strava import get_all_new_user_stats_from_strava
    from datetime import datetime

    # Google Sheet details
    google_sheet_key = '1i9D3SBDNKzLrP8ovrKwAuIZlvwCe0HBCPjfhEnHd01A'
    google_sheet_title = "SFB1425 ECS' CVHMM"
    google_sheet_name = 'Sheet1'

    # Init data from Google Sheet
    start_date_cell = 'B1'
    start_time_cell = 'D1'
    end_date_cell = 'E1'
    end_time_cell = 'H1'

    athlete_name_column = 1
    athlete_id_column = 2
    row_of_start_of_data = 3
    activity_col_dict = {"Run": 4, "Ride": 6,  # Dictionary containing the activity and the corresponding column number
                         "Walk": 7, "Swim": 9,
                         "Cumulative Elevation": 12,
                         "Cumulative Time": 13,
                         "Number of Activities": 14}

    # Strava details
    strava_client_id = 65701
    strava_client_secret = '60ed605025d846e6c580b66efc997b922cffd819'

    # Connect to the Google Sheet
    worksht = src.update_gspreadsheet.connect_to_gspreadsheet.authenticate_and_connect_to_gspreadsheet2(google_sheet_title, google_sheet_name)

    # Get starting date
    start_date = src.update_gspreadsheet.get_date_from_gspreadsheet.get_epoch_time_from_two_cells_in_googlespreadsheet(
        worksht,
        start_date_cell,
        start_time_cell
    )
    end_date = src.update_gspreadsheet.get_date_from_gspreadsheet.get_epoch_time_from_two_cells_in_googlespreadsheet(
        worksht,
        end_date_cell,
        end_time_cell
    )

    # Create data structures to store activity info
    # user_dict: list of users and their respective user_ids
    user_dict = src.update_gspreadsheet.get_users_and_user_ids_gspreadsheet.get_users_and_user_ids(worksht,
                                                                                                   athlete_name_column,
                                                                                                   athlete_id_column,
                                                                                                   row_of_start_of_data)
    #
    tally_dict = src.update_gspreadsheet.get_current_stats_from_gspreadsheet.get_current_stats_from_gspreadsheet(
        worksht,
        activity_col_dict,
        athlete_name_column,
        row_of_start_of_data)

    # Get user activities from Strava
    update_dict = src.update_strava.get_all_new_user_stats_from_strava.get_all_new_user_stats_from_strava(user_dict, strava_client_id, strava_client_secret, start_date, tally_dict)

    src.update_gspreadsheet.update_gspreadsheet_with_strava_data.update_gworksheet_with_strava_data(worksht, update_dict, activity_col_dict)

    last_update_time = datetime.now()
    print(f"Update done at {last_update_time}")


if __name__ == "__main__":
    main()
