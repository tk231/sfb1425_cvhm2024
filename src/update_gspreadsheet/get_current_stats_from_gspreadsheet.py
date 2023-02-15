def get_current_stats_from_gspreadsheet(worksheet, activity_dict, name_col, first_data_row):

    user_list = worksheet.col_values(name_col)[first_data_row:]
    user_run_list = worksheet.col_values(activity_dict['Run'])[first_data_row:]
    user_ride_list = worksheet.col_values(activity_dict['Ride'])[first_data_row:]
    user_walk_list = worksheet.col_values(activity_dict['Walk'])[first_data_row:]
    user_swim_list = worksheet.col_values(activity_dict['Swim'])[first_data_row:]
    user_elevation_list = worksheet.col_values(activity_dict['Cumulative Elevation'])[first_data_row:]
    user_time_list = worksheet.col_values(activity_dict['Cumulative Time'])[first_data_row:]
    user_freq_list = worksheet.col_values(activity_dict['Number of Activities'])[first_data_row:]

    # big_dict used to store all the data
    big_dict = {athlete: {'Run': run_val, 'Ride': ride_val, 'Walk': walk_val, 'Swim': swim_val, 'Cumulative Elevation': cuel_val, 'Cumulative Time': cutime_val, 'Number of Activities': act_val} for athlete, run_val, ride_val, walk_val, swim_val, cuel_val, cutime_val, act_val in zip(user_list, user_run_list, user_ride_list, user_walk_list, user_swim_list, user_elevation_list, user_time_list, user_freq_list)}

    return big_dict

