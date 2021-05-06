# Groupe 5
# Thomas CAPODANO
# Alexandre MARIE
# Sébastien POLIN-MARCILLY
# Chloé XAINTRAY

from board import Board
from computer import Computer,children_states
from game import Game


board = Board([-1, -2])
game = Game(board)
computer = Computer(board, game)
#print(children_states([1, 3]))
print(computer.minmax(board.state, 4))
#board.print()
