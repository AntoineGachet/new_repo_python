import copy
import time
import sys
import types
import weakref
from copyreg import dispatch_table
sys.setrecursionlimit(1958)

example_board = [
    [0,5,8, 0,0,0, 2,0,0],
    [0,0,0, 0,5,1, 8,0,0],
    [0,0,0, 2,6,0, 0,0,0],

    [0,1,4, 0,0,0, 0,5,9],
    [0,9,6, 0,2,0, 1,3,0],
    [8,3,0, 0,0,0, 7,4,0],

    [0,0,0, 0,9,6, 0,0,0],
    [0,0,2, 5,3,0, 0,0,0],
    [0,0,7, 0,0,0, 5,6,0],
]

the_first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
the_co_and_their_moves = {}
moves_to_play = []
the_co_and_their_recursions = {}
total_recursion = []




class Error(Exception):
    pass
error = Error   # backward compatibility

try:
    from org.python.core import PyStringMap
except ImportError:
    PyStringMap = None

__all__ = ["Error", "copy", "deepcopy"]

def copy(x):
    """Shallow copy operation on arbitrary Python objects.
    See the module's __doc__ string for more info.
    """

    cls = type(x)

    copier = _copy_dispatch.get(cls)
    if copier:
        return copier(x)

    try:
        issc = issubclass(cls, type)
    except TypeError: # cls is not a class
        issc = False
    if issc:
        # treat it as a regular class:
        return _copy_immutable(x)

    copier = getattr(cls, "__copy__", None)
    if copier:
        return copier(x)

    reductor = dispatch_table.get(cls)
    if reductor:
        rv = reductor(x)
    else:
        reductor = getattr(x, "__reduce_ex__", None)
        if reductor:
            rv = reductor(4)
        else:
            reductor = getattr(x, "__reduce__", None)
            if reductor:
                rv = reductor()
            else:
                raise Error("un(shallow)copyable object of type %s" % cls)

    if isinstance(rv, str):
        return x
    return _reconstruct(x, None, *rv)


_copy_dispatch = d = {}

def _copy_immutable(x):
    return x
for t in (type(None), int, float, bool, complex, str, tuple,
          bytes, frozenset, type, range, slice,
          types.BuiltinFunctionType, type(Ellipsis), type(NotImplemented),
          types.FunctionType, weakref.ref):
    d[t] = _copy_immutable
t = getattr(types, "CodeType", None)
if t is not None:
    d[t] = _copy_immutable

d[list] = list.copy
d[dict] = dict.copy
d[set] = set.copy
d[bytearray] = bytearray.copy

if PyStringMap is not None:
    d[PyStringMap] = PyStringMap.copy

del d, t

def deepcopy(x, memo=None, _nil=[]):
    """Deep copy operation on arbitrary Python objects.
    See the module's __doc__ string for more info.
    """

    if memo is None:
        memo = {}

    d = id(x)
    y = memo.get(d, _nil)
    if y is not _nil:
        return y

    cls = type(x)

    copier = _deepcopy_dispatch.get(cls)
    if copier:
        y = copier(x, memo)
    else:
        try:
            issc = issubclass(cls, type)
        except TypeError: # cls is not a class (old Boost; see SF #502085)
            issc = 0
        if issc:
            y = _deepcopy_atomic(x, memo)
        else:
            copier = getattr(x, "__deepcopy__", None)
            if copier:
                y = copier(memo)
            else:
                reductor = dispatch_table.get(cls)
                if reductor:
                    rv = reductor(x)
                else:
                    reductor = getattr(x, "__reduce_ex__", None)
                    if reductor:
                        rv = reductor(4)
                    else:
                        reductor = getattr(x, "__reduce__", None)
                        if reductor:
                            rv = reductor()
                        else:
                            raise Error(
                                "un(deep)copyable object of type %s" % cls)
                if isinstance(rv, str):
                    y = x
                else:
                    y = _reconstruct(x, memo, *rv)

    # If is its own copy, don't memoize.
    if y is not x:
        memo[d] = y
        _keep_alive(x, memo) # Make sure x lives at least as long as d
    return y

_deepcopy_dispatch = d = {}

def _deepcopy_atomic(x, memo):
    return x
d[type(None)] = _deepcopy_atomic
d[type(Ellipsis)] = _deepcopy_atomic
d[type(NotImplemented)] = _deepcopy_atomic
d[int] = _deepcopy_atomic
d[float] = _deepcopy_atomic
d[bool] = _deepcopy_atomic
d[complex] = _deepcopy_atomic
d[bytes] = _deepcopy_atomic
d[str] = _deepcopy_atomic
try:
    d[types.CodeType] = _deepcopy_atomic
except AttributeError:
    pass
d[type] = _deepcopy_atomic
d[types.BuiltinFunctionType] = _deepcopy_atomic
d[types.FunctionType] = _deepcopy_atomic
d[weakref.ref] = _deepcopy_atomic

def _deepcopy_list(x, memo, deepcopy=deepcopy):
    y = []
    memo[id(x)] = y
    append = y.append
    for a in x:
        append(deepcopy(a, memo))
    return y
d[list] = _deepcopy_list

def _deepcopy_tuple(x, memo, deepcopy=deepcopy):
    y = [deepcopy(a, memo) for a in x]
    # We're not going to put the tuple in the memo, but it's still important we
    # check for it, in case the tuple contains recursive mutable structures.
    try:
        return memo[id(x)]
    except KeyError:
        pass
    for k, j in zip(x, y):
        if k is not j:
            y = tuple(y)
            break
    else:
        y = x
    return y
d[tuple] = _deepcopy_tuple

def _deepcopy_dict(x, memo, deepcopy=deepcopy):
    y = {}
    memo[id(x)] = y
    for key, value in x.items():
        y[deepcopy(key, memo)] = deepcopy(value, memo)
    return y
d[dict] = _deepcopy_dict
if PyStringMap is not None:
    d[PyStringMap] = _deepcopy_dict

def _deepcopy_method(x, memo): # Copy instance methods
    return type(x)(x.__func__, deepcopy(x.__self__, memo))
d[types.MethodType] = _deepcopy_method

del d

def _keep_alive(x, memo):
    """Keeps a reference to the object x in the memo.
    Because we remember objects by their id, we have
    to assure that possibly temporary objects are kept
    alive by referencing them.
    We store a reference at the id of the memo, which should
    normally not be used unless someone tries to deepcopy
    the memo itself...
    """
    try:
        memo[id(memo)].append(x)
    except KeyError:
        # aha, this is the first one :-)
        memo[id(memo)]=[x]

def _reconstruct(x, memo, func, args,
                 state=None, listiter=None, dictiter=None,
                 deepcopy=deepcopy):
    deep = memo is not None
    if deep and args:
        args = (deepcopy(arg, memo) for arg in args)
    y = func(*args)
    if deep:
        memo[id(x)] = y

    if state is not None:
        if deep:
            state = deepcopy(state, memo)
        if hasattr(y, '__setstate__'):
            y.__setstate__(state)
        else:
            if isinstance(state, tuple) and len(state) == 2:
                state, slotstate = state
            else:
                slotstate = None
            if state is not None:
                y.__dict__.update(state)
            if slotstate is not None:
                for key, value in slotstate.items():
                    setattr(y, key, value)

    if listiter is not None:
        if deep:
            for item in listiter:
                item = deepcopy(item, memo)
                y.append(item)
        else:
            for item in listiter:
                y.append(item)
    if dictiter is not None:
        if deep:
            for key, value in dictiter:
                key = deepcopy(key, memo)
                value = deepcopy(value, memo)
                y[key] = value
        else:
            for key, value in dictiter:
                y[key] = value
    return y

del types, weakref, PyStringMap




def set_for_coordinates_their_moves_available(
    original_list,
    stored_coordinates
    ):
    # STEP 1: create the lists for each number to replace
    for row in range(9):
        for column in range(9):
            stored_coordinates[(row, column)] = copy.deepcopy(original_list)
    return stored_coordinates


def set_nb_recursion_for_this_co(
    the_co_and_their_recursions,
    total_recursion
    ):
    # STEP 1: create the lists for each number to replace
    for row in range(9):
        for column in range(9):
            the_co_and_their_recursions[(row, column)] = copy.deepcopy(total_recursion)
    return the_co_and_their_recursions


def get_moves_available(puzzle, stored_coordinates):
    set_for_coordinates_their_moves_available(the_first_list, the_co_and_their_moves)
    # STEP 2: store what moves are available in each row
    for check_row in range(9):
        for check_number in puzzle[check_row]:
            if check_number != 0:
                for delete_in_the_row in range(9):
                    try:
                        stored_coordinates[(check_row, delete_in_the_row)].remove(check_number)
                    except ValueError:
                        pass

    # STEP 3: store what moves are available in the columns
    for check_column in range(9):
        for determine_row in puzzle:
            if determine_row[check_column] != 0:
                for delete_in_the_column in range(9):
                    try:
                        stored_coordinates[(delete_in_the_column, check_column)].remove(determine_row[check_column])
                    except ValueError:
                        pass

    # STEP 4: store what moves are available in the square
    for center_row in range(1, 9, 3):
        for center_column in range(1, 9, 3):
            for check_adj_row in range(-1, 2, 1):
                for check_adj_column in range(-1, 2, 1):
                    nb_to_delete = puzzle[center_row + check_adj_row][center_column + check_adj_column]
                    if nb_to_delete != 0:
                        for delete_in_the_row in range(-1, 2, 1):
                            for delete_in_the_column in range(-1, 2, 1):
                                y_axis_delete = center_row + delete_in_the_row
                                x_axis_delete = center_column + delete_in_the_column
                                try:
                                    stored_coordinates[(y_axis_delete, x_axis_delete)].remove(nb_to_delete)
                                except ValueError:
                                    pass
    return stored_coordinates


def show_coo_and_moves(stored_coordinates):
    # show the coordinates and their available move
    get_moves_available(example_board, the_co_and_their_moves)
    for check_row in range(9):
        for check_column in range(9):
            print(check_row, check_column)
            print(stored_coordinates[(check_row, check_column)])


def find_empty(puzzle, move_to_replace):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                move_to_replace.append((i, j))  # row, col

    return move_to_replace


nb_to_check = -0
found_empty = find_empty(example_board, moves_to_play)
set_nb_recursion_for_this_co(the_co_and_their_recursions, total_recursion)
i = 0


def red_or_green_move(stored_coordinates, puzzle,
                      the_co_and_their_recursions, pos=None
                      ):
    get_moves_available(puzzle, stored_coordinates)

    if puzzle[8][8] != 0:
        print_board(puzzle)
        return puzzle
        exit()
    global i
    global nb_to_check
    global found_empty
    if nb_to_check < 0:
        exit()
    # find move to play
    i = i + 1
    print(i)
    # if i == 100:
    #     exit()
    if pos is None:
        pos = found_empty[nb_to_check]
    row, col = pos
    nb_moves = len(stored_coordinates[pos])
    nb_recursion = len(the_co_and_their_recursions[pos])
    print(found_empty[nb_to_check])
    print(stored_coordinates[pos])

    if nb_recursion >= nb_moves:
        # algo
        nb_to_check = nb_to_check-1
        previous_coordinates = found_empty[nb_to_check]
        the_co_and_their_recursions[pos].clear()
        new_row, new_col = previous_coordinates
        puzzle[row][col], puzzle[new_row][new_col] = 0, 0
        # just print board
        print_board(puzzle)
        print("\n", "\n")
        red_or_green_move(
            the_co_and_their_moves, example_board,
            the_co_and_their_recursions, previous_coordinates
            )

    if nb_moves == 1:
        # algo
        the_co_and_their_recursions[pos].extend("0")
        puzzle[row][col] = stored_coordinates[pos][0]
        # just print board
        print_board(puzzle)
        print("\n", "\n")
        nb_to_check += 1
        red_or_green_move(
            the_co_and_their_moves, example_board, the_co_and_their_recursions
            )

    elif nb_moves > 1:
        # algo
        the_co_and_their_recursions[pos].extend("0")
        puzzle[row][col] = stored_coordinates[pos][nb_recursion]
        # just print board
        print_board(puzzle)
        print("\n", "\n")
        nb_to_check += 1
        red_or_green_move(
            the_co_and_their_moves, example_board, the_co_and_their_recursions
            )

    elif nb_moves == 0:
        # algo
        nb_to_check = nb_to_check-1
        previous_coordinates = found_empty[nb_to_check]
        new_row, new_col = previous_coordinates
        puzzle[row][col] = 0
        # just print board
        print_board(puzzle)
        print("\n", "\n")
        red_or_green_move(
            the_co_and_their_moves, example_board,
            the_co_and_their_recursions, previous_coordinates
            )

    return puzzle


def print_board(puzzle):
    for i in range(len(puzzle)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(puzzle[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(puzzle[i][j])
            else:
                print(str(puzzle[i][j]) + " ", end="")


print_board(example_board)
print("_______________________")
red_or_green_move(
    the_co_and_their_moves, example_board, the_co_and_their_recursions
    )
