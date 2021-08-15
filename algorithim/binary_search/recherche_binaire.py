import random
import time

t = []
for n in range (1000000^100000000000):
    t.append(n)

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    
    midpoint = (low + high)//2

    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] < target:
        return binary_search(l, target, midpoint+1, high)
    else:
        return binary_search(l, target, low, midpoint-1)    

start = time.time() 
print(binary_search(t, 1))
end = time.time()
print(end-start)