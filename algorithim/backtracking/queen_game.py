dim1 = 5  # int(input('Enter the dimensions of your board: '))
board = [[' _ ' for n in range(dim1)] for i in range(dim1)]
rep = -1


def solve(dim, bo):
    global rep
    print(rep)

    for j in range(dim):
        if valid(dim, bo, rep, j):
            bo[rep][j] = ' d '
            show_board(dim1, bo)
            next_row(bo)

    else:
        bo[rep-1] == [' _ ' for n in range(dim)]
        rep -= 2
        solve(dim, bo)
    return True


def show_board(dim, bo):
    for x in range(dim):
        print("".join(bo[x]), end='\n')
    print('\n _________________________ \n')


def valid(dim, bo, row, col):
    # check row
    for x in range(dim):
        if bo[row][x] == ' d ':
            # print('o1')
            return False

    # check column
    for x in range(dim):
        if bo[x][col] == ' d ':
            # print('o2')
            return False

    # check left diagonals
    for i in range(row-dim, dim-col):
        try:
            if bo[row+i][col+i] == ' d ':
                # print('o3')
                return False
        except IndexError:
            break

    # check right diagonals
    for i in range(dim-col, row-dim, -1):
        try:
            if bo[row+i][col-i] == ' d ':
                # print('o4')
                return False
        except IndexError:
            break

    return True


def next_row(bo):
    global rep
    rep += 1
    return rep


show_board(dim1, board)
solve(dim1, board)
