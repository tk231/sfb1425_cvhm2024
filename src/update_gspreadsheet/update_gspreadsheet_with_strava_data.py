def update_gworksheet_with_strava_data(worksheet, update_dict, dict_activity_cols):
    import pandas

    start_row = 4

    # Convert update_dict to dataframe
    update_df = pandas.DataFrame.from_dict(update_dict, orient='index')

    # Update columns
    print("Updating sheet")
    run_update = worksheet.update(
        f"{dict_activity_cols['Run']}{start_row}:{dict_activity_cols['Run']}{start_row + update_df.shape[0] - 1}",
        [[val] for val in update_df["Run"].tolist()])
    cycle_update = worksheet.update(
        f"{dict_activity_cols['Ride']}{start_row}:{dict_activity_cols['Ride']}{start_row + update_df.shape[0] - 1}",
        [[val] for val in update_df["Ride"].tolist()])
    walk_update = worksheet.update(
        f"{dict_activity_cols['Walk']}{start_row}:{dict_activity_cols['Walk']}{start_row + update_df.shape[0] - 1}",
        [[val] for val in update_df["Walk"].tolist()])
    swim_update = worksheet.update(
        f"{dict_activity_cols['Swim']}{start_row}:{dict_activity_cols['Swim']}{start_row + update_df.shape[0] - 1}",
        [[val] for val in update_df["Swim"].tolist()])
    elevation_update = worksheet.update(
        f"{dict_activity_cols['Cumulative Elevation']}{start_row}:{dict_activity_cols['Cumulative Elevation']}{start_row + update_df.shape[0] - 1}",
        [[val] for val in update_df["Cumulative Elevation"].tolist()])
    time_update = worksheet.update(
        f"{dict_activity_cols['Cumulative Time']}{start_row}:{dict_activity_cols['Cumulative Time']}{start_row + update_df.shape[0] - 1}",
        [[val] for val in update_df["Cumulative Time"].tolist()])
    num_activities_update = worksheet.update(
        f"{dict_activity_cols['Number of Activities']}{start_row}:{dict_activity_cols['Number of Activities']}{start_row + update_df.shape[0] - 1}",
        [[val] for val in update_df["Number of Activities"].tolist()])

    return
