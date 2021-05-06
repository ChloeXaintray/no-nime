from players import Players


class Game:
    def __init__(self, board, turn=Players.PLAYER1):
        self.board = board
        self.turn = turn

    def check_winner(self, state):
        if state == 1:
            return Players.PLAYER1.value
        if state == -1:
            return Players.PLAYER2.value
        return 0
