# Groupe 5
# Thomas CAPODANO
# Alexandre MARIE
# Sébastien POLIN-MARCILLY
# Chloé XAINTRAY

from board import Board
from computer import Computer
from game import Game

board = Board([1, 3])
game = Game(board)
computer = Computer(board, game)
print(computer.minmax(board.state, 3))
#board.print()
