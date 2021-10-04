import random

array = []
for n in range(100):
    array.append(random.randint(0, 1000))


def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def sort(array, low, high):

    if len(array) == 1:
        return array

    if low < high:
        pi = partition(array, low, high)
        sort(array, low, pi - 1)
        sort(array, pi + 1, high)
    return array


print(sort(array, 0, len(array) - 1))
