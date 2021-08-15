def pendu(mot):
    mot = list(mot)
    mot_guess = []
    for i in range(len(mot)):
        mot_guess.append('_ ')
    n = 12
    while '_ ' in mot_guess:
        letter_guess = input('Une lettre ? : ')
        if n == 0:
            print('Trop tard... vous avez perdu')
            exit()
        if letter_guess in mot:
            if mot.count(letter_guess) > 1:
                for n in range(mot.count(letter_guess)):
                    letter = mot.index(letter_guess)
                    mot.pop(letter)
                    mot.insert(letter, ' ')
                    mot_guess[letter] = letter_guess
                print(''.join(mot_guess))
            if mot.count(letter_guess) == 1:
                letter = mot.index(letter_guess)
                mot_guess[letter] = letter_guess
                print(''.join(mot_guess))
        else:
            n = n-1
            print('Aïe... vous n''avez pluse que', n, 'chance')
            print(''.join(mot_guess))
    print('Bravo vous avez gagné, le mot est : ')
    print(''.join(mot_guess))


pendu("element")
