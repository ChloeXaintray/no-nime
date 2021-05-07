import random
from typing import Tuple
from players import Players
from static import explain_state, children_states, check_winner
from tqdm import tqdm

class Computer:
    def __init__(self, board, game):
        self.board = board
        self.game = game
        self.scores = {}

    def get_best_move(self, node, depth):
        print(node)
        state, mark = explain_state(node)
        temp = None
        for child in children_states(state, mark):
            temp = child
            print(" child ")
            print(child)
            if self.minmax(child, depth) == mark.value:
                return child
        return temp

    def compute_heuristic(self, n: int, state: Tuple):
        print("heuristic")
        player_wins = 0
        for i in range(n):
            current_state = tuple(state)
            while check_winner(current_state) == 0:
                (temp_state, mark) = explain_state(current_state)
                random_row = random.randrange(len(temp_state))
                random_sticks = random.randrange(1, temp_state[random_row] + 1)
                temp_list = list(temp_state)
                temp_list[random_row] -= random_sticks  # pick the sticks
                temp_list = list(filter(lambda x: x != 0, temp_list))

                if len(temp_list) == 0:
                    if mark == Players.PLAYER:
                        player_wins += 1
                    break

                temp_list[0] *= -mark.value
                current_state = tuple(temp_list)

        percent = player_wins / n

        if percent > 0.5:
            return 1
        return -1

    def minmax(self, node, depth):
        """
        print('--------------------------')
        print(node)
        print(depth)
        """

        if check_winner(node) != 0:
            return check_winner(node)
        if depth == 0:
            return self.compute_heuristic(50, node)

        state, mark = explain_state(node)

        if mark == Players.COMPUTER:
            maximum = -2
            for child in children_states(state, mark):
                if child not in self.scores:
                    maximum = max(maximum, self.minmax(child, depth - 1))
                    self.scores[child] = maximum
                else:
                    maximum = self.scores[child]

            return maximum
        else:
            minimum = 2
            for child in children_states(state, mark):
                if child not in self.scores:
                    minimum = min(minimum, self.minmax(child, depth - 1))
                    self.scores[child] = minimum
                else:
                    minimum = self.scores[child]
            return minimum
