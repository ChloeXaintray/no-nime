# Groupe 5
# Thomas CAPODANO
# Alexandre MARIE
# Sébastien POLIN-MARCILLY
# Chloé XAINTRAY

from board import Board
from game import Game
from players import Players

board = Board([-1, 2])
game = Game(board)
game.play(Players.COMPUTER)

