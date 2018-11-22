""" Game class """
import os
import sys
from .logger import log

class Game():
    """ Class representing a game to be run """

    def __init__(self, game_id):
        log.debug('Initializing Game')
        self.game_id = game_id
        self.env = os.environ

        # create self.args and pop the script off
        self.args = sys.argv
        self.args.pop(0)

        # put on the brakes and to avoid fork bomb
        assert 'steamfixes' not in self.args[0]
        assert 'python' not in self.args[0]

        self.cmd = self.args[0]

    def run(self):
        """ Start the game """

        # exec call must be used here or the process will be caught by loader.so again
        os.execvp(self.cmd, self.args)
