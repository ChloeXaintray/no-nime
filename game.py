from computer import Computer, explain_state
from players import Players
from static import check_winner
import time


class Game:
    def __init__(self, board, turn=Players.COMPUTER):
        self.board = board
        self.turn = turn

    def play_computer(self, computer):
        computer.reset_score()
        computer.reset_cpt_minmax()

        start_time = time.time()
        if check_winner(self.board.state) != 0:
            return
        self.board.print()
        print("COMPUTER is playing ...")

        move = computer.get_best_move(self.board.state, 30)
        if move == -1 or move == 1:
            self.board.state = -1
        else:
            self.board.set_state(list(move))
        print("--- %s seconds ---" % (time.time() - start_time))
        print("cpt minmax: ", computer.cpt_minmax)

    def play_player(self):
        if check_winner(self.board.state) != 0:
            return
        self.board.print()
        print("PLAYER is playing ...")

        row = input("Enter the row:  ")
        while not row.isnumeric() or int(row) < 1 or int(row) > len(self.board.state):
            row = input("Please enter a VALID row:  ")
        row = int(row)

        sticks = input("Enter a number of sticks:  ")
        while not sticks.isnumeric() or int(sticks) < 1 or int(sticks) > abs(self.board.state[row-1]):
            sticks = input("Please enter a VALID number of sticks:  ")
        sticks = int(sticks)

        current_board = list(self.board.state)
        if row == 1:
            _, mark = explain_state(self.board.state)
            current_board[row - 1] -= sticks * (-mark.value)
        else:
            current_board[row - 1] -= sticks
        self.board.set_state(current_board)

        if len(self.board.state) == 0:
            self.board.state = 1

    def play(self, starter=Players.COMPUTER):
        computer = Computer(self.board, self)
        computer2 = Computer(self.board, self)

        # while check_winner(self.board.state) == 0:
        #     if starter.value == 1:
        #         self.play_computer(computer)
        #         self.play_player()
        #     else:
        #         self.play_player()
        #         self.play_computer(computer)

        while check_winner(self.board.state) == 0:
            self.play_computer(computer)
            self.play_computer(computer2)

        if check_winner(self.board.state) == 1:
            print("\n---Computer wins---")
        else:
            print("\n---Player wins---")


