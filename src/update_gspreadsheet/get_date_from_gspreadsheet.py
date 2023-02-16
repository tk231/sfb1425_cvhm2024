def get_epoch_time_from_two_cells_in_googlespreadsheet(worksheet, datecell):
    from datetime import datetime
    import pandas

    # For date only use below
    # date = datetime.strptime(worksheet.acell(datecell).value, "%Y-%m-%d").date()

    # For datetime use below
    date = datetime.strptime(worksheet.acell(datecell).value, "%Y-%m-%d")
    # TODO: include timecell
    date_iso = date.isoformat()
    # Always return in ISO 8601 format

    return date_iso
