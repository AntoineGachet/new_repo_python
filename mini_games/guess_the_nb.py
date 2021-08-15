import random

a = random.randrange(1, 101)
user_guess = int(input('Entrer votre guess'))

while user_guess != a:
    if user_guess < a:
        user_guess = int(input("Le nombre est plus GRAND"))
    if user_guess > a:
        user_guess = int(input('Le nombre est plus PETIT'))
    else:
        print('Vous avez gagné')
