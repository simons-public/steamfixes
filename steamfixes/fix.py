""" Runs games with fixes """
from .logger import log
from .game import Game
from .util import game_id

def run():
    """ Loads a gamefix module by it's game id """
    log.info('Running game ' + game_id())
    if not game_id():
        return

    game = Game(game_id)
    game.run()
