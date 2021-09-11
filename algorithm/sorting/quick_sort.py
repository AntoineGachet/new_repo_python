array = [43, 2, 64, 87, 25, 99, 34, 31, 71]


def partition(array, low, high):
    i = low - 1
    pivot = array[-1]
    pivot_index = -1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            swap(array, j, i)

    swap(array, pivot_index, i + 1)
    return i + 1


def sort(array, low, high):

    if len(array) == 1:
        return array
    if low < high:
        pi = partition(array, low, high)
    sort(array, low, pi - 1)
    sort(array, pi + 1, high)

    return array


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


print(sort(array, 0, len(array)))
