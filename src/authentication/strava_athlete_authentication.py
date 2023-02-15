# Needs to be run within 15 mins of the user requesting the token
# DO NOT RUN AGAIN FOR USER WHO IS ALREADY AUTHENTICATED!

# URL for authorisation: https://www.strava.com/oauth/authorize?client_id=[CLIENT_ID]&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:read_all,activity:read_all
# code is from the URL of the authorisation page

def main():
    import requests
    import json  # Make Strava auth API call with your

    json_folder = '/mnt/Aruba/PyCharmProjects/strava_club_challenge_automated/logins/strava'
    athlete_code = ''  # From authorisation URL

    # client_code, client_secret and code
    response = requests.post(
        url='https://www.strava.com/oauth/token',
        data={
            'client_id': 65701,  # INSERT_CLIENT_ID_HERE
            'client_secret': '60ed605025d846e6c580b66efc997b922cffd819',  # INSERT_CLIENT_SECRET_KEY
            'code': athlete_code,  # INSERT_CODE_FROM_URL_HERE
            'grant_type': 'authorization_code'
        }
    )

    # Save json response as a variable
    strava_token = response.json()  # Save tokens to file

    athelete_id = strava_token['athlete']['id']

    with open(f"{json_folder}/strava_token_{athelete_id}.json", "w") as outfile:
        json.dump(strava_token, outfile)


if __name__ == "__main__":
    main()