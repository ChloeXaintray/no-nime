# Groupe 5
# Thomas CAPODANO
# Alexandre MARIE
# Sébastien POLIN-MARCILLY
# Chloé XAINTRAY

from board import Board
from game import Game
from players import Players

board = Board([-1, 3, 5, 7, 13, 15, 18])
game = Game(board)
game.play(Players.PLAYER)

