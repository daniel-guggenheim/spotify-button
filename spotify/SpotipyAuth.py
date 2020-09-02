import string

import spotipy

from helper import env_var
from spotify.CustomAuthManager import CustomAuthManager

# Env var to set
SPOTIFY_USERNAME = 'SPOTIFY_USERNAME'
SPOTIPY_CLIENT_ID = 'SPOTIPY_CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'SPOTIPY_CLIENT_SECRET'
SPOTIPY_REFRESH_TOKEN = 'SPOTIPY_REFRESH_TOKEN'
SPOTIPY_REDIRECT_URI = 'SPOTIPY_REDIRECT_URI'


def spotify_client(scope: string) -> spotipy.client.Spotify:
    keys = {
        'username': env_var(SPOTIFY_USERNAME),
        'client_id': env_var(SPOTIPY_CLIENT_ID),
        'client_secret': env_var(SPOTIPY_CLIENT_SECRET),
        'refresh_token': env_var(SPOTIPY_REFRESH_TOKEN),
        'redirect_uri': env_var(SPOTIPY_REDIRECT_URI)
    }
    return spotipy.Spotify(auth_manager=CustomAuthManager(scope, keys))
