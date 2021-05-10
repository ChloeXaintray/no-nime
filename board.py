import random


class Board:
    def __init__(self):
        #row_list =[-1, 3, 5, 7, 13, 15, 18]
        row_list = []

        user_choice = input("Enter 1 to generate a random board, 2 to create it: ")
        while not user_choice.isnumeric() or int(user_choice) < 1 or int(user_choice) > 2:
            user_choice = input("Enter 1 or 2 ")
        user_choice = int(user_choice)
        print(user_choice)

        if user_choice == 1:

            rows = random.randrange(1, 10, 1)
            for i in range(rows):
                stick = random.randrange(1, 100, 1)
                row_list.append(int(stick))
        else:
            rows = input("Enter a number of row (between 1 and 10):  ")
            while not rows.isnumeric() or int(rows) < 1 or int(rows) > 10:
                rows = input("Enter a VALID number of rows:  ")
            rows = int(rows)

            for i in range(rows):
                print("Row ", i + 1)
                stick = input("Enter a number of stick (between 1 and 100):  ")
                while not stick.isnumeric() or int(stick) < 1 or int(stick) > 100:
                    stick = input("Enter a VALID number of rows:  ")
                row_list.append(int(stick))

        row_list[0] *= -1
        print(row_list)

        self.state = None
        self.set_state(row_list)

    def set_state(self, row_list):
        row_list.sort()
        self.state = tuple(filter(lambda x: x != 0, row_list))

    def print(self):
        print(self.state)
        for index, value in enumerate(self.state) :
            print(index+1, " : ", abs(value)*"|", " (", f"{(abs(value))}", ")")
        print("")
