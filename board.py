class Board:
    def __init__(self, row_list):
        self.state = None
        self.set_state(row_list)

    def set_state(self, row_list):
        row_list.sort()
        self.state = tuple(filter(lambda x: x != 0, row_list))

    def print(self):
        for index, value in enumerate(self.state) :
            print(index, " : ", abs(value)*"|", " (", f"{(abs(value))}", ")")
        print("")