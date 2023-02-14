# Needs to be run within 15 mins of the user requesting the token
# DO NOT RUN AGAIN FOR USER WHO IS ALREADY AUTHENTICATED!

# URL for authorisation: https://www.strava.com/oauth/authorize?client_id=[CLIENT_ID]&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:read_all,activity:read_all
# code is from the URL of the authorisation page

import requests
import json  # Make Strava auth API call with your

# client_code, client_secret and code
response = requests.post(
    url='https://www.strava.com/oauth/token',
    data={
        'client_id': 65701,  # INSERT_CLIENT_ID_HERE
        'client_secret': '60ed605025d846e6c580b66efc997b922cffd819',  # INSERT_CLIENT_SECRET_KEY
        'code': 'e9108174521db5245e1aa5ad0ae1a17fc891ce5a',  # INSERT_CODE_FROM_URL_HERE
        'grant_type': 'authorization_code'
    }
)  # Save json response as a variable

strava_tokens = response.json()  # Save tokens to file
# with open(f'strava_tokens_8981968.json', 'w') as outfile:
#     json.dump(strava_tokens, outfile)  # Open JSON file and print the file contents
#
# # to check it's worked properly
# with open('strava_tokens_8981968.json') as check:
#     data = json.load(check)
#
# print(data)
