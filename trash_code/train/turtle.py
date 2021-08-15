def carré2(c,couleur):
    
    color(couleur)
    for i in range(4):
        forward(c)
        right(90)
    left(0)
    for i in range(3):
        forward(c)
        left(120)
    right(90)
    forward(c)
    right(-30)
    for i in range(3):
        forward(c)
        left(120)
        
        
