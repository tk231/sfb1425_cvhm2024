def get_epoch_time_from_two_cells_in_googlespreadsheet(spreadsheet, datecell, timecell):
    import datetime

    date = datetime.strptime(spreadsheet.acell(datecell).value, "%Y-%m-%d").date()

    # Always return as epoch time
    return date.timestamp()
