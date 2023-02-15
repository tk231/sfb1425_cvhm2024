def get_epoch_time_from_two_cells_in_googlespreadsheet(worksheet, datecell):
    from datetime import datetime
    import pandas

    date = datetime.strptime(worksheet.acell(datecell).value, "%Y-%m-%d").date()
    # TODO: include timecell
    date_iso = date.isoformat()
    # Always return in ISO 8601 format

    return date_iso
