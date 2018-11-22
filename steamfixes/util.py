""" Various utilities used by steamfixes """
import os

def game_id():
    """ Caches and returns the SteamAppId as """
    return os.environ.get('SteamAppId')
