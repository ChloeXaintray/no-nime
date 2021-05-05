def children_states(state):
    children = []
    for index, value in enumerate(state):
        for i in range(value):
            new_state = list(state)
            new_state[index] = i
            if 0 in new_state:# and len(new_state) > 1:
                new_state.remove(0)
            children.append(tuple(new_state))
    return children


class Computer:
    def __init__(self, board, game):
        self.board = board
        self.game = game

    def minmax(self, node, depth, maximizing_player=True):
        """
        print('--------------------------')
        print(node)
        print(depth)
        """
        if depth == 0 or self.game.check_loser(node) != 0:
            # print("cas arret")
            return  0 # heuristic
        if maximizing_player:
            maximum = -2
            for child in children_states(node):
                maximum = max(maximum, self.minmax(child, depth - 1, False))
            return maximum
        else:
            minimum = -2
            for child in children_states(node):
                minimum = min(minimum, self.minmax(child, depth - 1, True))
            return minimum
