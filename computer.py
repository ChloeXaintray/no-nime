class Computer:

    def __init__(self, board, game):
        self.board = board
        self.game = game

    def children_states(self):
        children = []
        for index,value in enumerate(self.board.state):
            for i in range(value):
                new_state = list(self.board.state)
                new_state[index] = i
                children.append(tuple(new_state))
        return children

    #def minmax(self, node, depth, maximizing_player):
    #    if depth == 0 or node
