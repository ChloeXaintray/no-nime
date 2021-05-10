import random
from typing import Tuple

import static
from players import Players
from static import explain_state, children_states, check_winner, is_winning_board

NHEURISTIC = 20
DEPTH = 3

class Computer:
    def __init__(self, board, game):
        self.board = board
        self.game = game
        self.scores = {}
        self.cpt_minmax = 0

    def get_best_move(self, node):
        state, mark = explain_state(node)
        temp = None
        value = self.minmax(node, DEPTH, -2, 2)
        print("score : ",value)

        for child in children_states(state, mark):
            temp = child
            if self.minmax(child, DEPTH-1, -2, 2) == value:
                return child
        return temp

    def compute_heuristic(self, n: int, state: Tuple):
        cpt_victory = 0
        for i in range(n):
            current_state = tuple(state)
            while check_winner(current_state) == 0:
                (temp_state, mark) = explain_state(current_state)
                if is_winning_board(temp_state):
                    if mark == Players.COMPUTER:
                        cpt_victory += 1
                    break

                random_row = random.randrange(len(temp_state))
                random_sticks = random.randrange(1, temp_state[random_row] + 1)
                temp_list = list(temp_state)
                temp_list[random_row] -= random_sticks  # pick the sticks
                temp_list = list(filter(lambda x: x != 0, temp_list))

                if len(temp_list) == 0:
                    if mark == Players.PLAYER:
                        cpt_victory += 1
                    break

                temp_list[0] *= -mark.value
                current_state = tuple(temp_list)

        percent = cpt_victory / (2*n)
        return percent*2-1

    def minmax(self, node, depth, alpha, beta):
        if node in self.scores:
            return self.scores[node]

        if check_winner(node) != 0:
            return check_winner(node)

        self.cpt_minmax += 1

        if depth == 0:
            self.scores[node] = self.compute_heuristic(NHEURISTIC, node)
            return self.scores[node]

        state, mark = explain_state(node)
        if mark == Players.COMPUTER:
            maximum = -2
            for child in children_states(state, mark):
                maximum = max(maximum, self.minmax(child, depth - 1, alpha, beta))
                alpha = max(maximum, alpha)
                if alpha >= beta:
                    break
            self.scores[node] = maximum
            return maximum
        else:
            minimum = 2
            for child in children_states(state, mark):
                minimum = min(minimum, self.minmax(child, depth - 1, alpha, beta))
                beta = min(minimum, beta)
                if beta <= alpha:
                    break
            self.scores[node] = minimum
            return minimum

    def reset_score(self):
        self.scores = {}

    def reset_cpt_minmax(self):
        self.cpt_minmax = 0
