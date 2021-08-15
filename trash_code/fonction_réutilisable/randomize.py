from math import*

def random_quote (my_list):
    rand_numb=random.randint(0,len(my_list)-1)
    item=my_list[rand_numb]
    return item
