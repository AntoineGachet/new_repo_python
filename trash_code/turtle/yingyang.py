from turtle import*
def yingyang  (c,couleur):

    circle (c)
    circle(c/2,180)
    circle(-c/2,180)
    up()
    goto(0,0)
    left(90)
    forward(c/2-c/20)
    right(90)
    forward(c/20)
    down()
    circle(c/10)
    up()
    goto(0,0)
    left(90)
    forward(c+c/2)
    forward(c/20+c/20)
    down()
    circle(c/10)
    
    
