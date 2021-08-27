import random


def who_wins(nb_joueur):
    able_moves = ['cisors', 'paper', 'rock']
    if nb_joueur == 1:
        user_move = input('rock, paper, cisors ? ')
        move2 = random.randrange(len(able_moves))
        computer_move = able_moves[move2]
        while computer_move == user_move:
            move2 = random.randrange(len(able_moves)) 
            computer_move = able_moves[move2]

    elif nb_joueur == 0:
        move1 = random.randrange(len(able_moves)-1)
        user_move = able_moves[move1]
        move2 = random.randrange(len(able_moves))
        computer_move = able_moves[move2]
        while computer_move == user_move:
            move2 = random.randrange(len(able_moves)) 
            computer_move = able_moves[move2]
            move1 = random.randrange(len(able_moves))
            user_move = able_moves[move1]

    if computer_move == 'cisors' and user_move == 'paper':
        print(computer_move, 'gangre contre', user_move)
    elif computer_move == 'cisors' and user_move == 'rock':
        print(user_move, ' gagne contre', computer_move)
    elif computer_move == 'paper' and user_move == 'rock':
        print(computer_move, 'gagne contre ', user_move)
    elif computer_move == 'paper' and user_move == 'cisors':
        print(user_move, ' gagne contre ', computer_move)
    elif computer_move == 'rock' and user_move == 'cisors':
        print(computer_move, 'gagne contre', user_move)
    elif computer_move == 'rock' and user_move == 'paper':
        print(user_move, ' gagne contre ', computer_move)


who_wins(0)