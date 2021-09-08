import random
import time


def binary_search(len_tree):
    start = time.time()
    right_nb = random.randrange(len_tree+1)
    tree = []
    n = -1

    while len(tree) < len_tree:
        n+=1
        tree.append(n)
    computer_move = len_tree
  
    while computer_move != right_nb:
        print(right_nb)
        if computer_move < right_nb:
            for n in range(tree[0], computer_move+1):
                print(tree)
                tree.remove(n)
            computer_move = tree[(len(tree)-2)//2]
            print(computer_move)
        if computer_move > right_nb:
            for n in range(tree[len(tree)-1], computer_move-1, -1):
                print(tree)
                tree.remove(n)
            computer_move = tree[(len(tree)-2)//2]
            print(computer_move)
    
    end = time.time()
    print('Le nombre était', right_nb)
    print(end-start)


print(binary_search(1000000))
