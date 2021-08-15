from turtle import*
from math import*

def coeur(c,color):
    begin_fill()
    left(90)
    circle(c/2,180)
    left(180)
    circle(c/2,180)
    left(30)
    forward(280)
    left(117)
    forward(295)
    end_fill()
