import random

k = [random.randint(0, 100) for x in range(100)]


def swap(array, value_1, value_2):
    array[value_1], array[value_2] = array[value_1], array[value_1]


def bubble_sort(array):
    for values in range(len(array)):
        try:
            if array[values] > array[values + 1]:
                swap(array, values, values + 1)
                print(array)
        except IndexError:
            return array


print(bubble_sort(k))
