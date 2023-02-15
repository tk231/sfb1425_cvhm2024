# From https://github.com/mkl1288/strava_club_challenge/blob/784fe54d34e7c956704f6be513dfa083bd067dc2/run_strava_club_challenge_in_google_sheets.py#L23
def connect_to_gspreadsheet(key: str, worksheetname: str):
    import gspread

    # connect to google sheet
    gc = gspread.oauth(credentials_filename='/mnt/Aruba/PyCharmProjects/strava_club_challenge_automated/logins/gsheet/client_secret_520138570687-4e7tlu697n14cpfildf7ghjbpbgdml7a.apps.googleusercontent.com.json')
                       # authorized_user_filename='/mnt/Aruba/PyCharmProjects/strava_club_challenge_automated/logins'
                       #                          '/gsheet/authorized_user.json')

    # open worksheet
    worksheet = gc.open_by_key(key).worksheet(worksheetname)

    return worksheet


def connect_to_gspreadsheet2(key: str, worksheetname: str):
    import gspread
    import google.oauth2.credentials

    credentials = google.oauth2.credentials.Credentials(
        'access_token',
        refresh_token='1//09UWFp7FSIQ0-CgYIARAAGAkSNwF-L9IrEoGksI_c3B3nA5gVAQbgSbGKTO8kvXqbFxeTqOYas2UAGZd3v1xdu2UGtq7jovYKvCs',
        token_uri='https://oauth2.googleapis.com/token',
        client_id='520138570687-4e7tlu697n14cpfildf7ghjbpbgdml7a.apps.googleusercontent.com',
        client_secret='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'
    )
    client = gspread.authorize(credentials)
    sheet = client.open(key).worksheet(worksheetname)
    return sheet
