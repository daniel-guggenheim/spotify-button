import os

from spotify.AddCurrent import AddCurrent
from spotify.DeleteRecent import DeleteRecent
from spotify.SpotipyAuth import spotify_auth


def env_var(var_name):
    return os.environ.get(var_name, f'Environment variable "{var_name}" is not set.')


# Env vars
SCOPE = "user-read-playback-state,user-modify-playback-state,playlist-read-private,playlist-modify-private"
USERNAME = env_var('SPOTIFY_USERNAME')
PLAYLIST_ID = env_var('PLAYLIST_ID')

# Init spotify client and helper classes
spotify_client = spotify_auth(scope=SCOPE, username=env_var(USERNAME))
delete_function = DeleteRecent(spotify_client)
add_function = AddCurrent(spotify_client)


def add_current_music(request):
    print(request)
    add_function.add_current_music(PLAYLIST_ID)
    return 200


def delete_recently_added_song(request):
    print(request)
    delete_function.delete_recently_added_song(PLAYLIST_ID)
    return 200
