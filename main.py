import json

from helper import env_var
from spotify.AddCurrent import AddCurrent
from spotify.DeleteRecent import DeleteRecent
from spotify.SpotipyAuth import spotify_client
from flask import abort
import logging

# Request variables
TOKEN_REQ = 'token'
ADD_CURRENT_REQ = 'add'
DELETE_RECENT_REQ = 'delete'

# Env vars
SCOPE = "user-read-playback-state,user-modify-playback-state,playlist-read-private,playlist-modify-private"
PLAYLIST_ID = env_var('PLAYLIST_ID')
APP_SECRET = env_var('APP_SECRET')

# Init spotify client and helper classes
spotify_client = spotify_client(scope=SCOPE)
delete_function = DeleteRecent(spotify_client)
add_function = AddCurrent(spotify_client)


def main(request):
    request_args = request.args
    logging.info(request_args)
    if not is_authenticated(request_args):
        return abort(401, "Unauthorized request.")

    try:
        if ADD_CURRENT_REQ in request_args:
            add_function.add_current_music(PLAYLIST_ID)
            return "add successful"
        elif DELETE_RECENT_REQ in request_args:
            delete_function.delete_recently_added_song(PLAYLIST_ID)
            return "delete successful"
        else:
            return abort(400, f"Bad request, must be one of [{ADD_CURRENT_REQ}, {DELETE_RECENT_REQ}]")
    except Exception as e:
        return abort(500, "Internal error. Exception: " + str(e))


def is_authenticated(request_args):
    return request_args and 'token' in request_args and request_args['token'] == APP_SECRET

def add_current_music(request):
    add_function.add_current_music(PLAYLIST_ID)
    return str(json.dumps(request))


def delete_recently_added_song(request):
    print(request)
    delete_function.delete_recently_added_song(PLAYLIST_ID)
    return str(json.dumps(request))
