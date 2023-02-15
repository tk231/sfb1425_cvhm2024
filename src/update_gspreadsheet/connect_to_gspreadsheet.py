# From https://github.com/mkl1288/strava_club_challenge/blob/784fe54d34e7c956704f6be513dfa083bd067dc2/run_strava_club_challenge_in_google_sheets.py#L23
def connect_to_gspreadsheet(key: str, worksheetname: str):
    import gspread

    # connect to google sheet
    gc = gspread.oauth()

    # open worksheet
    worksheet = gc.open_by_key(key).worksheet(worksheetname)

    return worksheet
