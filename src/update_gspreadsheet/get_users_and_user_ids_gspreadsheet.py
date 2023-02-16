# Gets the current stats of all athletes in spreadsheet
def get_users_and_user_ids(worksheet, name_col, id_col, first_data_row):
    athlete_list = worksheet.col_values(name_col)[first_data_row:]
    athlete_id_list = worksheet.col_values(id_col)[first_data_row:]

    user_dict = dict(zip(athlete_list, athlete_id_list))

    return user_dict
