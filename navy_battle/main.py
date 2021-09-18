class Game:
    def __init__(self):
        self.board = []

    def create_board(self):

        row = []
        for i in range(11):
            for j in range(10):
                if len(self.board) == 0:
                    row.append("%c) " % (j + 65))
                else:
                    row.append("  |")
            self.board.append(row)
            if i != 0:
                self.board[i].insert(0, f"{i}) ") if i != 10 else self.board[i].insert(
                    0, f"{i})"
                )
            else:
                self.board[0].insert(i, "  ")
            row = []
        return self.board


class Boats(Game):
    def __init__(self):
        self.little_boat = None
        self.mid_boat = None
        self.big_boat = None
        self.huge_boat = None

    def well_placed(self, boat):
        co1, co2 = boat
        if co1[0] != co2[0] and co1[1] != co2[1]:
            print("wrong")
            return False
        return True

    def place_boat(self):
        placed = False
        while not placed:
            boat = str(input("Where do u want to place your first boat: A1, D1 "))
            boat = tuple(x for x in boat.split(","))
            if Boats.well_placed(self, boat):
                placed = True


a = Game()
bo = a.create_board()

b = Boats()
b.place_boat()


def print_bo(board):
    for i in range(len(board)):
        print("".join(board[i]))


print(print_bo(bo))
