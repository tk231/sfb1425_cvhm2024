# From https://github.com/mkl1288/strava_club_challenge/blob/784fe54d34e7c956704f6be513dfa083bd067dc2/run_strava_club_challenge_in_google_sheets.py#L23
def authenticate_and_connect_to_gspreadsheet(key: str, worksheetname: str):
    # Guide for Google oauth and apis: https://medium.com/@ashokyogi5/a-beginners-guide-to-google-oauth-and-google-apis-450f36389184
    import httplib2

    from oauth2client.client import flow_from_clientsecrets
    from oauth2client.file import Storage
    from oauth2client.tools import run_flow
    import google.auth

    client_secret = ''
    scope = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    storage = Storage(
        '')

    credentials = storage.get()
    if credentials is None or credentials.invalid:
        flow = flow_from_clientsecrets(client_secret, scope=scope)
        http = httplib2.Http()
        credentials = run_flow(flow, storage, http=http)
    return credentials

    # connect to google sheet
    # gc = gspread.Client(auth=)

    # open worksheet
    worksheet = gc.open_by_key(key).worksheet(worksheetname)

    return worksheet

def connect_to_gspreadsheet2(key: str, worksheetname: str):
    import gspread
    import google.oauth2.credentials

    credentials = google.oauth2.credentials.Credentials(
        'access_token',
        refresh_token='',
        token_uri='',
        client_id='',
        client_secret=''
    )
    client = gspread.authorize(credentials)
    sheet = client.open(key).worksheet(worksheetname)
    return sheet

def authenticate_and_connect_to_gspreadsheet2(worksheetname: str, sheet: str):
    # Only working version of the function
    import gspread

    credentials = {"installed":
                       {"client_id": "",
                        "project_id": "",
                        "auth_uri": "",
                        "token_uri": "",
                        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                        "client_secret": "",
                        "redirect_uris": ["http://localhost"]
                        }
                   }

    gc, authorized_user = gspread.oauth_from_dict(credentials)

    worksheet = gc.open(worksheetname).worksheet(sheet)

    return worksheet
