import random

# ask the board dimensions
board = []
nb_check = -0


the_board = []
nb_row = int(input("Combien de rangées souhaitez vous ?: "))
nb_column = int(input("Combien de columns souhaitez vous ?: "))
nb_bomb = int(
    input("Combien de bombes voulez vous ?" "Plus il y en a plus le jeu est dur: ")
)

# create the nb of row
for n in range(nb_row):
    the_board.append([])
    # create the column
    for i in range(nb_column):
        the_board[n].append("   |")

the_board.insert(0, [])
# give the x cooardinate
for n in range(1, nb_column + 1):
    if n >= 10:
        the_board[0].append(f" {n})")
    else:
        the_board[0].append(f"  {n})")

# give the y cooardinate
for n in range(nb_row + 1):
    the_board[n].insert(0, " ")
for n in range(1, nb_row + 1):
    if n >= 10:
        the_board[n][0] = f"{n})"
    else:
        the_board[n][0] = f"{n}) "

# prevent the indexerror
the_board.append([])
for n in range(nb_column+2):
    the_board[nb_row+1].insert(n, "")
for n in range(nb_row+1):
    the_board[n].append("")

no_bomb = []

# create the bomb
for n in range(nb_bomb):
    x_axis = random.randrange(1, nb_column + 1)
    y_axis = random.randrange(1, nb_row + 1)
    the_board[y_axis][x_axis] = "   ⁢⁢⁢⁢⁢|"


def check_if_bomb(wich_row=None, wich_column=None):
    global nb_check
    global no_bomb
    # allows the function to be call back
    if wich_row is None:
        wich_row = int(input("Choose your row: "))
        wich_column = int(input("Choose your column: "))
        nb_check = 0
        no_bomb = []
    counter = 0
    # stop the game if the player choose a bomb
    if the_board[wich_row][wich_column] == "   ⁢⁢⁢⁢⁢|":
        print("You've lost :(")
        exit()
    # check the 3 rows
    for n in range(1, -2, -1):
        # check the columns
        for i in range(1, -2, -1):
            # give the nb of bomb next to the user move
            if the_board[wich_row - n][wich_column - i] == "   ⁢⁢⁢⁢⁢|":
                counter = counter + 1
    # reusing the same loop but after one is done prevent the function to be called if there's a bomb nearby
    for n in range(1, -2, -1):
        # check the columns
        for i in range(1, -2, -1):
            # callback the function if there is a value = 0
            if the_board[wich_row - n][wich_column - i] == "   |" and counter == 0:
                coordinates = (wich_row - n, wich_column - i)
                # store the coordinates inside a tuple to reuse them
                if no_bomb.count(coordinates) == 0:
                    no_bomb.append(coordinates)
    the_board[wich_row][wich_column] = f" {counter} |"
    # make the function work when it should
    for i in range(nb_check, len(no_bomb)):
        if the_board[wich_row][wich_column] == " 0 |":
            nb_check += 1
            check_if_bomb(no_bomb[i][0], no_bomb[i][1])
        else:
            break


while True:
    for n in range(nb_row + 2):
        showed_board = "".join(the_board[n])
        print(showed_board)
    print(no_bomb)
    check_if_bomb()

