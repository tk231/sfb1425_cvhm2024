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

### Setting Up Strava App

Benji Knights Johnson made a good guide as to how to connect to Strava's API. The connection is performed by:

1. Creating an App. Under website, only a URL that is of a URL structure has to be inputted. The `Autorization Callback Domain` only has to be filled with `localhost`.

2. Authentication
