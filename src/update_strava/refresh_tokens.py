def refresh_tokens(token: dict, strava_client_id: int, strava_client_secret: str) -> dict:
    """
    Refresh the Strava access token using the given refresh token, client ID, and client secret.

    Parameters:
    -----------
    token : dict
        Dictionary containing the existing Strava token information, including the refresh token.
    strava_client_id : int
        The Strava client ID used to refresh the access token.
    strava_client_secret : str
        The Strava client secret used to refresh the access token.

    Returns:
    --------
    dict
        A dictionary containing the new access token and other token-related information.

    Description:
    ------------
    This function sends a POST request to the Strava OAuth token endpoint to refresh the access token.
    It requires the `strava_client_id`, `strava_client_secret`, and `refresh_token` from the `token` parameter.

    If the response status code is 200, indicating success, the function returns the new token information as a JSON dictionary.
    If the request fails, an appropriate error handling mechanism (not shown here) should be implemented.

    Note:
    -----
    - The function expects a valid refresh token in the `token` dictionary.
    - Proper error handling should be implemented to manage cases when the token refresh fails.
    - This function requires the `requests` library for HTTP requests.
    """
    import requests

    # Make new request
    response = requests.post(
        url='https://www.strava.com/oauth/token',
        data={
            'client_id': strava_client_id,
            'client_secret': strava_client_secret,
            'grant_type': 'refresh_token',
            'refresh_token': token['refresh_token']
        }
    )
    
    if response.status_code == 200:
        new_strava_token = response.json()

    return new_strava_token