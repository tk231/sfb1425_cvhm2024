def update_gworksheet_with_strava_data(worksheet, update_dict, activity_dict):
    import pandas

    run_col = 'D'
    cycle_col = 'F'
    walk_col = 'G'
    swim_col = 'I'
    elevation_col = 'L'
    time_col = 'M'
    num_of_activities_col = 'N'

    start_row = 4

    # Convert update_dict to dataframe
    update_df = pandas.DataFrame.from_dict(update_dict, orient='index')

    # Update columns
    print("Updating sheet")
    run_update = worksheet.update(f"{run_col}{start_row}:{run_col}{start_row + update_df.shape[0] - 1}",
                                  [[val] for val in update_df["Run"].tolist()])
    cycle_update = worksheet.update(f"{cycle_col}{start_row}:{cycle_col}{start_row + update_df.shape[0] - 1}",
                                    [[val] for val in update_df["Ride"].tolist()])
    walk_update = worksheet.update(f"{walk_col}{start_row}:{walk_col}{start_row + update_df.shape[0] - 1}",
                                   [[val] for val in update_df["Walk"].tolist()])
    swim_update = worksheet.update(f"{swim_col}{start_row}:{swim_col}{start_row + update_df.shape[0] - 1}",
                                   [[val] for val in update_df["Swim"].tolist()])
    elevation_update = worksheet.update(
        f"{elevation_col}{start_row}:{elevation_col}{start_row + update_df.shape[0] - 1}",
        [[val] for val in update_df["Cumulative Elevation"].tolist()])
    time_update = worksheet.update(f"{time_col}{start_row}:{time_col}{start_row + update_df.shape[0] - 1}",
                                   [[val] for val in update_df["Cumulative Time"].tolist()])
    num_activities_update = worksheet.update(
        f"{num_of_activities_col}{start_row}:{num_of_activities_col}{start_row + update_df.shape[0] - 1}",
        [[val] for val in update_df["Number of Activities"].tolist()])

    return
