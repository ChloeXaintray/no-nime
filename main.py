# Groupe 5
# Thomas CAPODANO
# Alexandre MARIE
# Sébastien POLIN-MARCILLY
# Chloé XAINTRAY

from board import Board
from computer import Computer
from game import Game
from players import Players

test = Board([1, 3, 5, 7])
test.print()

game = Game(test)
computer = Computer(test, game)

result = computer.compute_heuristic(1000, (1, 3, 5), Players.PLAYER1)
print(result * 100, "%")