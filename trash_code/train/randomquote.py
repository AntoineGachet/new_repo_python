quote1=["j'aime la langue de molière","je n'aime pas la langue de molière"]
cersos=["alvin","patrcik","tracer","harry"]

user_answer=input("si vous aimez la citation appuyez sur B pour terminer le programme, si celle-ci ne vous plait pas alors appuyez sur C")

import random

def random_quote (my_list):
    rand_numb=random.randint(0,len(my_list)-1)
    item=my_list[rand_numb]
    return item

def capitalize(quote1,cersos):
    
    capitalize(quote1)
    capitalize(cersos)
    return "{} a dit: {}".format (cersos,quote1)


while user_answer != "B":
    print(random_quote(cersos),random_quote(quote1))
    user_answer=input("si vous aimez la citation appuyez sur B pour terminer le programme, si celle-ci ne vous plait pas alors appuyez sur C")
