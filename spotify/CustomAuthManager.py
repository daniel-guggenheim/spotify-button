import datetime

from spotipy.oauth2 import SpotifyOAuth


class CustomAuthManager:
    """
    Code inspired from https://github.com/plamere/spotipy/issues/555#issuecomment-675099233
    """

    def __init__(self, scope, keys):
        self.auth = SpotifyOAuth(scope=scope,
                                 client_id=keys['client_id'], client_secret=keys['client_secret'],
                                 redirect_uri=keys['redirect_uri'], username=keys['username'])
        self.refresh_token = keys['refresh_token']
        self.current_token = None

    def get_access_token(self):
        now = datetime.datetime.now()

        # if no token or token about to expire soon
        if not self.current_token or self.current_token['expires_at'] < now.timestamp() + 60:
            self.current_token = self.auth.refresh_access_token(self.refresh_token)

        return self.current_token['access_token']
