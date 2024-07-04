# Dash Dashboard for Group Strava Activity

## Credits

This project has been massively helped by the following people:

* Felix Flath (felix.flath@uniklinik-freiburg.de);
* Joachim Greiner (joachim.greiner@uniklinik-freiburg.de);
* Pavamkumar Videm (videmp@informatik.uni-freiburg.de);
* the Early Career Scientists from CRC1425.

## Introduction

This project has been changed heavily for the event held. The following states the major changes:

* Instead of uploading to a Google Sheets, the program now displays the data on a webpage (hosted by PythonAnywhere);
* Instead of running the entire script every time to update the data and the table, a script has to be run once to create the main data table, and another every time the data table has to be updated;
* Instead of tracking kilometers, kilocalories are tracked;
* Script now based on `requests` library.

This project collates data from athletes' Strava account after the application has been authorised. The data is then organised by activities, which are then displayed in on a Dash table.

## Setup

### Folder Structure

First, clone project. The project folder should look like the following:

```
strava_club_challenge_automated
├── assets
│   ├── athlete_access_tokens
│   └── strava_app.yaml
├── dash_folder
│   ├── 0_frontpage.py
│   ├── 1_table.py
│   ├── 2_athlete_comparison.py
│   └── 3_activity_breakdown.py
├── data
├── resources
│   ├── athlete_access_tokens
│   └── strava_app.yaml
├── src
│   ├── authentication
│   │   ├── __init__.py
│   │   └── strava_athlete_authentication.py
│   ├── update_strava
│   │   ├── __init__.py
│   │   ├── get_activity_dataframe.py
│   │   ├── only_update_pickles_and_data_table.py
│   │   └── refresh_tokens.py
│   └── __init__.py
├── main.py
└── README.md
```

#### Assets

Contains the assets needed for the webpage, e.g.: logos.

#### Dash Folder

Contains the files needed for the Dash dashboard. These are used in `main.py`. The main pages are a front page, `frontpage.py` and `table.py`. Additional data analysis pages can be added.

#### Data

Contains a folder called `athlete_pickles`, where the individual athlete pickles are stored within. Additionally, pickle containing all the collated data, `final_table_pickle.pkl`, and an Excel table listing all the athletes, their teams, and their Strava IDs, `athlete_database.xlsx`, are also stored here.

#### Resources

Contains the folder `athlete_access_tokens`, where the athlete access tokens are stored. Additionally, a `yaml` file containing the Strava app's `strava_client_id` and `strava_client_secret` is also stored here.

#### Source

Contains the script(s) for authenticating individual athletes and to update or to create the initial table. 

### Python Anywhere Hosting

TODO

### Athletes' Authorisation

For the application to have the permission to scrape data from an athlete's Strava profile, the athlete first has to authorise the application:

1. The athlete has to first click on the following link:
    > https://www.strava.com/oauth/authorize?client_id=[CLIENT_ID]&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:read_all,activity:read_all
2. After approving the app, the athlete would be redirected to an empty page;
3. The link would have to be copied and pasted into the script in `src.authentication.strava_athlete_authentication.py`;
4. If the authorisation was successful, one would receive a status code 200 and the access token would be stored in `json_path`;

If authorisation was unsuccessful, check if the required fields were authorised.

### Creation of Initial Data Table

TODO

### Updating of Data Table

Run `src.update_strava.only_update_pickles_and_data_table.py` when table should be updated. This is done a number of times daily. Update and refresh app on PythonAnywhere.

### Adding New Athletes

After the data table `final_table_pickle.pkl` has been created, new participants can be retroactively added:

1. Authorise athlete as per above steps;
2. Add athlete and athlete ID (and team) into `athlete_database.xlsx`;
3. Run `src.update_strava.only_update_pickles_and_data_table.py`.

## Room for Improvement

The following items could be improved on (based on feel and user feedback):
* Improve look and formatting of table;
* Improve user authorisation process;
* Automation of updating process, perhaps to make it inline with Strava's recommendation of using webhooks.