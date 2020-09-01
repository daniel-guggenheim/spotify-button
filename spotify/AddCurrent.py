import string

import spotipy

from spotify.SoundSignal import failure_command_signal, successful_command_signal


class AddCurrent:

    def __init__(self, spotify_client: spotipy.client.Spotify):
        self.sp = spotify_client

    def add_current_music(self, my_playlist_id: string):
        current_music_id = self.__get_current_music_played_id()
        if self.__in_playlist(my_playlist_id, current_music_id):
            failure_command_signal(self.sp)
            return
        self.__add_music_to_playlist(my_playlist_id, current_music_id)
        successful_command_signal(self.sp)

    def __get_current_music_played_id(self):
        return self.sp.current_playback()['item']['id']

    def __in_playlist(self, my_playlist_id: string, current_music_id: string):
        offset = 0

        while True:
            tracks_in_playlist_chunk = self.sp.playlist_items(my_playlist_id, offset=offset,
                                                              fields='items.track.id,total',
                                                              additional_types=['track'])

            offset = offset + len(tracks_in_playlist_chunk['items'])
            if len(tracks_in_playlist_chunk['items']) == 0:
                break

            # Check if current_music_id in tracks
            for track in tracks_in_playlist_chunk['items']:
                if current_music_id == track['track']['id']:
                    return True
        return False

    def __add_music_to_playlist(self, my_playlist_id: string, current_music_id: string):
        items = [current_music_id]
        self.sp.playlist_add_items(my_playlist_id, items)
