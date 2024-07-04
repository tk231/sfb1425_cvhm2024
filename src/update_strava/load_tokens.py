def load_token(token_path: str, strava_client_id: int, strava_client_secret: str) -> dict:
    """
    Load Strava access token from a JSON file and refresh it if it has expired.

    Parameters:
    -----------
    token_path : str
        The file path to the JSON file containing the Strava access token and refresh token.
    strava_client_id : int
        The Strava client ID used for refreshing the access token.
    strava_client_secret : str
        The Strava client secret used for refreshing the access token.

    Returns:
    --------
    dict
        A dictionary containing the refreshed or existing access token along with other token details.

    Description:
    ------------
    This function reads the Strava token from a JSON file specified by `token_path`.
    If the token has expired (based on the `expires_at` field), it uses the refresh token
    to obtain a new access token. If the token is still valid, it returns the existing one.

    To refresh the token, the function relies on an external `refresh_tokens` function,
    providing the necessary client ID and client secret for authentication.

    Usage:
    ------
    Use this function to ensure you have a valid access token for making requests to the
    Strava API. If the token has expired, it is refreshed automatically.
    """
    import json
    import time

    import src.update_strava.refresh_tokens

    # Open json file to connect to Strava
    with open(token_path, mode='r') as json_file:
        strava_token = json.load(json_file)

    # If access_token has expired, use refresh_token to get new access_token
    if strava_token['expires_at'] < time.time():
        # Make new request
        token = src.update_strava.refresh_tokens.refresh_tokens(strava_token, strava_client_id, strava_client_secret)

    else:
        token = strava_token

    return token