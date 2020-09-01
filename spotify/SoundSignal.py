import time

import spotipy


def successful_command_signal(client: spotipy.client.Spotify):
    current_volume = client.current_playback()['device']['volume_percent']
    client.volume(int(current_volume * 3 / 4))
    time.sleep(0.6)
    client.volume(current_volume)


def failure_command_signal(client: spotipy.client.Spotify):
    current_volume = client.current_playback()['device']['volume_percent']
    client.volume(int(current_volume * 1 / 2))
    time.sleep(0.5)
    client.volume(int(current_volume * 1 / 5))
    time.sleep(0.5)
    client.volume(current_volume)
