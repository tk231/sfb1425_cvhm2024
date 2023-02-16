def update_gworksheet_with_strava_data(worksheet, update_dict, activity_dict):
    # update_dict contains all the cumulative distances of all users
    for user in update_dict:
        # Row and cell coordinates allow for continuity with gspread's syntax
        user_row = worksheet.find(user).row

        user_activity_dict = update_dict[user]
        # user_activity_dict contains the cumulative distances of single user
        for activity in user_activity_dict:
            worksheet.update_cell(user_row, activity_dict[activity], user_activity_dict[activity])

    return
