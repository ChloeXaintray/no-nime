from game import Game
from board import Board
import random


class Computer:

    def __init__(self, board, game):
        self.board = board
        self.game = game

    def compute_heuristic(self, number, state, player):
        player_wins = 0
        for i in range(number):
            random_game = Game(Board(list(state)), self.game.turn)
            while random_game.check_loser(random_game.board.state) == 0:
                current_board = list(random_game.board.state)
                random_row = random.randrange(len(current_board))
                sticks_to_pick = random.randrange(1, current_board[random_row] + 1)
                current_board[random_row] -= sticks_to_pick

                random_game.board.set_state(current_board)  # reminder: auto sort and remove 0 done in this method
                random_game.next_turn()

            if not random_game.check_loser(random_game.board.state) == player.value:
                print("you win")
                player_wins += 1
            else:
                print("you loose")
        return player_wins / number
