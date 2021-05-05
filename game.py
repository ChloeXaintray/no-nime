from players import Players

class Game:

    def __init__(self, board, turn=Players.PLAYER1):
        self.board = board
        self.turn = turn

    def check_loser(self, state):
        if state == ():
            return self.turn.value
        return 0

    def next_turn(self):
        if self.turn == Players.PLAYER1:
            self.turn = Players.PLAYER2
        else:
            self.turn = Players.PLAYER1
