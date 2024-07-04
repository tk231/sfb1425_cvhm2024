# Needs to be run within 15 mins of the user requesting the token
# DO NOT RUN AGAIN FOR USER WHO IS ALREADY AUTHENTICATED!

# URL for authorisation: https://www.strava.com/oauth/authorize?client_id=[
# CLIENT_ID]&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile
# :read_all,activity:read_all code is from the URL of the authorisation page

def main():
    import requests
    import json  # Make Strava auth API call with your
    import yaml

    path_to_strava_app_yaml = ''
    json_folder = 'resources/athlete_access_tokens'
    athlete_code = ''  # From authorisation URL

    # Load strava_app_yaml
    strava_app_deets = yaml.load(open(path_to_strava_app_yaml), Loader=yaml.Loader)

    # client_code, client_secret and code
    response = requests.post(
        url='https://www.strava.com/oauth/token',
        data={
            'client_id': strava_app_deets['strava_client_id'],  # INSERT_CLIENT_ID_HERE
            'client_secret': strava_app_deets['strava_client_secret'],  # INSERT_CLIENT_SECRET_KEY
            'code': athlete_code,  # INSERT_CODE_FROM_URL_HERE
            'grant_type': 'authorization_code'
        }
    )

    if response.status_code == 200:
        print(f"Status code 200 received, saving json")
        # Save json response as a variable
        strava_token = response.json()  # Save tokens to file

        athelete_id = strava_token['athlete']['id']

        with open(f"{json_folder}/strava_token_{athelete_id}.json", "w") as outfile:
            json.dump(strava_token, outfile)

    else:
        print(f"Error {response.status_code}: {response.reason}")


if __name__ == "__main__":
    main()
