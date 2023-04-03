def get_epoch_time_from_two_cells_in_googlespreadsheet(worksheet, datecell, timecell):
    from datetime import datetime

    # For date only use below
    # date = datetime.strptime(worksheet.acell(datecell).value, "%Y-%m-%d").date()

    # For datetime use below
    date_str = worksheet.acell(datecell).value
    time_str = worksheet.acell(timecell).value

    if (date_str or time_str) == 'End':
        print(f"Cell {datecell} or {timecell} is empty!")
        return

    else:
        date = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")
        date_iso = date.isoformat()

    return date_iso
