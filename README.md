# Combining Strava and Google Sheets for Club Challenges

## Resources

Here are the resources that were used in these projects:

* [How To Automate a Club Challenge with Strava and Google Sheets, for Dummies](https://python.plainenglish.io/how-to-automate-a-club-challenge-with-strava-and-google-sheets-for-dummies-3c9ebc018781) by Maggie L. Her repository is found [here](https://github.com/mkl1288/strava_club_challenge).

* She uses a script by Benji Knights Johnson, details may be found [here](https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86).

## Setup

### Google Sheet Setup

A Google Sheet was created. The following fields were required:

![Screenshot from 2023-02-06 13-52-47](https://user-images.githubusercontent.com/49594308/216977021-64031d84-4c88-454d-b1b1-4aa82ee9b08f.png)

The ID of the Google Sheet document, i.e.: the string between `/d/` and `/edit`, was noted. It would be referred to as `google_sheet_id` in the proceeding text. 

The `Athlete ID` numbers have to be searched one by one. It can be found in the URL of the athlete: `https://www.strava.com/athletes/[STRAVA_ID]`.

The API for Google Sheets is done with [`gspread` 5.7.0](https://docs.gspread.org/en/v5.7.0/). One has to first authenticate and authorise the application. A quick guide to do this is found in `gspread`'s documentation under ["Authentication"](https://docs.gspread.org/en/v5.7.0/oauth2.html). After obtaining the OAuth credentials, a dictionary of the `.json` file contents were made, and subsequently used for authorising the app. In the programme, this was done like this (almost exactly the same as in the `gspread` documentation):

```
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
```

### Setting Up Strava App

Benji Knights Johnson made a good guide as to how to connect to Strava's API. The connection is performed by:

1. Creating an App. Under website, only a URL that is of a URL structure has to be inputted. The `Autorization Callback Domain` only has to be filled with `localhost`.

2. Authentication. See Maggie L.'s description on how it was done. This was very well documented. However, the code to save Strava tokens (i.e.: the `.json` response) should be changed to ensure that the tokens are saved in a secure location. Athletes only have to be authenticated once with the code in `src.authentication.strava_athlete_authentication`, running it again for the same athlete "forces the token to expire" and the authentification has to be done again. 

## Rest of the Code

