# Groupe 5
# Thomas CAPODANO
# Alexandre MARIE
# Sébastien POLIN-MARCILLY
# Chloé XAINTRAY

from board import Board
from game import Game
from players import Players
from static import children_states


board = Board()
game = Game(board)
game.play(Players.COMPUTER)


