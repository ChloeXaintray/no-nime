from players import Players


def explain_state(state):
    if state[0] < 0:
        temp_state = list(state)
        temp_state[0] = - temp_state[0]
        return tuple(temp_state), Players.PLAYER1
    return state, Players.PLAYER2


def children_states(state, mark):
    children = []
    for index, value in enumerate(state):
        for i in range(value):
            new_state = list(state)
            new_state[index] = i
            if 0 in new_state:
                new_state.remove(0)
            if len(new_state) > 0:
                new_state[0] *= mark.value
                children.append(tuple(new_state))
            else:
                children.append(-mark.value)

    return children


class Computer:
    def __init__(self, board, game):
        self.board = board
        self.game = game

    def get_computer_moves(self, node, depth):
        children_path = {}
        state, mark = explain_state(node)
        for child in children_states(state, mark):
            children_path[child] = self.minmax(child, depth)
        return children_path


    def minmax(self, node, depth):
        """
        print('--------------------------')
        print(node)
        print(depth)
        """

        if self.game.check_winner(node) != 0:
            return self.game.check_winner(node)
        if depth == 0:
            return 0  # heuristic

        state, mark = explain_state(node)

        if mark == Players.PLAYER1:
            maximum = -2
            for child in children_states(state, mark):
                maximum = max(maximum, self.minmax(child, depth - 1))
            return maximum
        else:
            minimum = 2
            for child in children_states(state, mark):
                minimum = min(minimum, self.minmax(child, depth - 1))
            return minimum
