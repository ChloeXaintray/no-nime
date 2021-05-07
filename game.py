from computer import Computer, explain_state
from players import Players
from static import check_winner



class Game:
    def __init__(self, board, turn=Players.COMPUTER):
        self.board = board
        self.turn = turn

    def play_computer(self, computer):
        if check_winner(self.board.state) != 0:
            return
        self.board.print()
        print("COMPUTER is playing ...")

        move = computer.get_best_move(self.board.state, 20)
        if move == -1 or move == 1:
            self.board.state = -1
        else:
            self.board.set_state(list(move))


    def play_player(self):
        if check_winner(self.board.state) != 0:
            return
        self.board.print()
        print("PLAYER is playing ...")

        row = int(input("Enter the row:  "))
        while row < 1 or row > len(self.board.state):
            row = int(input("Please enter a VALID row:  "))


        sticks = int(input("Enter a number of sticks:  "))
        while sticks < 1 or sticks > abs(self.board.state[row-1]):
            sticks = int(input("Please enter a VALID number of sticks:  "))

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
        
        while check_winner(self.board.state) == 0:
            if starter.value == 1:
                self.play_computer(computer)
                self.play_player()
            else :
                self.play_player()
                self.play_computer(computer)

        if check_winner(self.board.state) == 1:
            print("\n---Computer wins---")
        else:
            print("\n---Player wins---")
