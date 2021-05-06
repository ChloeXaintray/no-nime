from computer import Computer, explain_state
from players import Players
from static import check_winner


class Game:
    def __init__(self, board, turn=Players.PLAYER1):
        self.board = board
        self.turn = turn

    def play_computer(self, computer):
        print("COMPUTER PLAYS :")

        move = computer.get_best_move(self.board.state, 16)
        if move == -1 or move == 1:
            self.board.state = -1
        else:
            self.board.set_state(list(move))



    def play_player(self):
        print("PLAYER PLAYS :")

        row = int(input("Enter the row:  "))
        sticks = int(input("Enter number of sticks:  "))

        current_board = list(self.board.state)
        if row == 1:
            _, mark = explain_state(self.board.state)
            current_board[row-1] -= sticks*(-mark.value)
        else:
            current_board[row - 1] -= sticks
        self.board.set_state(current_board)

        if len(self.board.state) == 0:
            self.board.state = 1


    def play(self):
        computer = Computer(self.board, self)
        
        while check_winner(self.board.state) == 0:
            self.board.print()
            self.play_computer(computer)
            if check_winner(self.board.state) == 0:
                self.board.print()
                self.play_player()

        if check_winner(self.board.state) == 1:
            print("---Player1 is winner---")
        else:
            print("---Player2 is winner---")
