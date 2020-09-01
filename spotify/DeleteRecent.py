import string
from datetime import datetime, timezone, timedelta
from typing import Dict

import spotipy

from spotify.SoundSignal import successful_command_signal, failure_command_signal


class DeleteRecent:
    RECENT_TIME_DELTA = timedelta(minutes=15)

    def __init__(self, spotify_client: spotipy.client.Spotify):
        self.sp = spotify_client

    def delete_recently_added_song(self, my_playlist_id: string):
        nb_items_playlist = self.__get_nb_tracks_playlist(my_playlist_id)
        last_added_song = self.__get_last_added_song_to(my_playlist_id, nb_items_playlist)

        if self.__recently_added(last_added_song):
            self.__delete_track_fom(my_playlist_id, last_added_song, nb_items_playlist - 1)
            successful_command_signal(self.sp)
        else:
            failure_command_signal(self.sp)

    def __get_nb_tracks_playlist(self, my_playlist_id: string):
        return self.sp.playlist(my_playlist_id)['tracks']['total']

    def __get_last_added_song_to(self, my_playlist_id: string, nb_items_playlist: string):
        playlist_items = self.sp.playlist_items(my_playlist_id, limit=1, offset=nb_items_playlist - 1)
        return playlist_items['items'][0]

    def __delete_track_fom(self, my_playlist_id: string, track: Dict, position: int):
        track_uri = track['track']['id']
        items = [{'uri': track_uri, 'positions': [position]}]
        self.sp.playlist_remove_specific_occurrences_of_items(my_playlist_id, items)

    @staticmethod
    def __recently_added(last_added_song: Dict):
        added_at = datetime.strptime(last_added_song['added_at'], "%Y-%m-%dT%H:%M:%S%z")
        now = datetime.now(timezone.utc)
        return now - added_at < DeleteRecent.RECENT_TIME_DELTA
