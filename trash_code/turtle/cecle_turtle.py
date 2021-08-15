from turtle import*
def rosace(c,couleur):
    for i in range (4):
        circle(c)
        goto(0,0)
        left(90)

def carréchelou(c,color,x):
    for i in range(36):
        for i in range(1,x+1):
            forward(c)
            left(360/i)
    
