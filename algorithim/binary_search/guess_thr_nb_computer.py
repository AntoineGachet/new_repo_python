import random

a = random.randrange(1, 101)
computer_guess = random.randrange(1, 101)

while a != computer_guess:
    print(a)
    print(computer_guess)
    if computer_guess > a:
        computer_guess = random.randrange(1, computer_guess)
    if computer_guess < a:
        computer_guess = random.randrange(computer_guess, 100)
    if computer_guess == a:
        print('Bravo !!!', computer_guess)
