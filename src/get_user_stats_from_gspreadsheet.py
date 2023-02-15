def get_user_stats_from_gspreadsheet(worksheet, activity_dict, name_col, first_data_row):

    user_list = worksheet.col_values(name_col)[first_data_row:]
    user_run_list = worksheet.col_values(activity_dict['Run'])[first_data_row:]
    user_ride_list = worksheet.col_values(activity_dict['Ride'])[first_data_row:]
    user_walk_list = worksheet.col_values(activity_dict['Walk'])[first_data_row:]
    user_swim_list = worksheet.col_values(activity_dict['Swim'])[first_data_row:]
    user_elevation_list = worksheet.col_values(activity_dict['Cumulative Elevation'])[first_data_row:]
    user_time_list = worksheet.col_values(activity_dict['Cumulative time'])[first_data_row:]
    user_freq_list = worksheet.col_values(activity_dict['Number of Activities'])[first_data_row:]

    # big_dict used to store all the data
    big_dict = {}

    # Input the data from the spreadsheet into a nested dictionary
    # TODO: test
    for athlete in user_list:
        big_dict[athlete]['Run'] = user_run_list[athlete]
        big_dict[athlete]['Ride'] = user_ride_list[athlete]
        big_dict[athlete]['Walk'] = user_walk_list[athlete]
        big_dict[athlete]['Swim'] = user_swim_list[athlete]
        big_dict[athlete]['Cumulative Elevation'] = user_elevation_list[athlete]
        big_dict[athlete]['Cumulative time'] = user_time_list[athlete]
        big_dict[athlete]['Number of Activities'] = user_freq_list[athlete]

    return big_dict

