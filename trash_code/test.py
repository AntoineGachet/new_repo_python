import random

#create the machine to put inside the system
def machine1(a,b):
    if a==0:
        a=1
    else:
        a=0
    return a,b  
def machine2(a,b):
    if b==0:
        b=1
    else:
        b=0
    return a,b       
def machine3(a,b):
    c=b
    b=a
    a=c
    return a,b
def machine4(a,b):
    a=a*b
    b=b
    return a,b
def machine5(a,b):
    b=a*b
    a=a
    return a,b

machinerandom = [machine1(machine2(machine3(machine4(machine5(0,1)))))]
