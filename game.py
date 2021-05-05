from players import Players
from computer import Computer


class Game:

    def __init__(self, board, turn=Players.PLAYER1):
        self.board = board
        self.turn = turn

    def check_winner(self):
        if self.board.state == (1,):
            return self.turn.value
        return 0
