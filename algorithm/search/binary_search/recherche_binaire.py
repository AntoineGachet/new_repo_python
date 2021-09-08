import random
import time


nb = random.randint(0, 1000)
print(nb)


def binary_search(lenth, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = lenth
    midpoint = (low + lenth) // 2
    # print(nb)
    if midpoint == nb:
        return midpoint
    elif midpoint > nb:
        new_high = midpoint
        binary_search(midpoint, low, new_high + 1)
    else:
        new_low = midpoint
        binary_search(nb, new_low + 1, high)


binary_search(1000)
