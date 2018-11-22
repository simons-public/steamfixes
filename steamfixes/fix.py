""" Runs games with fixes """

import os
import sys
from importlib import import_module
from .logger import log
from .game import Game
from .util import game_id

def run():
    """ Loads a gamefix module by it's game id """
    log.info('Running game ' + game_id())
    if not game_id():
        return

    game = Game(game_id())

    localpath = os.path.expanduser('~/.local/share/steamfixes/localfixes')
    if os.path.isfile(os.path.join(localpath, game_id() + '.py')):
        sys.path.append(os.path.expanduser('~/.local/share/steamfixes'))
        try:
            game_module = import_module('localfixes.' + game_id())
            game_module.main(game)
        except ImportError:
            pass
    else:
        try:
            game_module = import_module('steamfixes.gamefixes.' + game_id())
            game_module.main(game)
            print('loaded module')
        except ImportError:
            pass

    game.run()

