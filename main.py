# Groupe 5
# Thomas CAPODANO
# Alexandre MARIE
# Sébastien POLIN-MARCILLY
# Chloé XAINTRAY

from board import Board
from game import Game
from players import Players


board = Board()
game = Game(board)
game.play(Players.PLAYER)

