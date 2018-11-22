""" Torchlight II """

def main(game):
    game.env['LD_PRELOAD'] += '/usr/lib/libcurl.so.3'
