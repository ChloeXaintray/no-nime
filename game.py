from players import Players

class Game:

    def __init__(self, board, turn=Players.PLAYER1):
        self.board = board
        self.turn = turn

    def check_loser(self, state):
        if state == (0,):
            return self.turn.value
        return 0
