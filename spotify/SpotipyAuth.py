import string

import spotipy
from spotipy.oauth2 import SpotifyOAuth


def spotify_auth(scope: string, username: string) -> spotipy.client.Spotify:
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, username=username))
