regles = "pour choisir votre coup, vous tapez la position dans le jeu, les positions se décomposent en : première ligne = position1, postion2, position3 etc..."
print(regles)

user1 = input("Entrez le nom du premier joueur : ")
user2 = input("Entrez le nom du deuxième joueur : ")

# créée le tableau
row1 = ["   ", "|", "   ", "|", "  "]
row2 = ["   ", "|", "   ", "|", "  "]
row3 = ["   ", "|", "   ", "|", "  "]
mid_row1 = "-----------"

# créée les listes qui permettent la vérification
diagonale1 = []
diagonale2 = []
vertical_row1 = []
vertical_row2 = []
vertical_row3 = []

# print le tableau
print("".join(row1))
print(mid_row1)
print("".join(row2))
print(mid_row1)
print("".join(row3))

# permet aux joueurs de jouer tour à tour
for i in range(9):
    # vérifie si user1 a gagné
    if row1.count(" o ") == 3 or row2.count(" o ") == 3 or row3.count(" o ") == 3 or diagonale1.count(" o ") == 3 or diagonale2.count(" o ") == 3 or vertical_row1.count(" o ") == 3 or vertical_row2.count(" o ") == 3 or vertical_row3.count(" o ") == 3:
        print("Bravo vous avez gagné ")
        exit()

    play1 = int(input("Que le premier joueur joue son coup : "))

    # vérifie sur quelle ligne le coup de user1 est joué
    if play1 == 1:
        
        vertical_row2.append(" x ")
        vertical_row1.append(" x ")
        row1[play1 - 1] = " x "
        diagonale1.append(" x ")
    elif play1 == 2:
        row1[play1] = " x "
        vertical_row2.append(" x ")
    elif play1 == 3:
        vertical_row3.append(" x ")
        diagonale2.append(" x ")
        row1[play1 + 1] = " x "
    if play1 == 4:
        row2[play1 % 3 - 1] = " x "
        vertical_row1.append(" x ")
    elif play1 == 5:
        row2[play1 % 3] = " x "
        vertical_row2.append(" x ")
        diagonale1.append(" x ")
        diagonale2.append(" x ")
    elif play1 == 6:
        vertical_row3.append(" x ")
        row2[play1 // 2 + 1] = " x "
    if play1 == 7:
        row3[play1 % 3 - 1] = " x "
        vertical_row1.append(" x ")
        diagonale2.append(" x ")
    elif play1 == 8:
        row3[play1 % 3] = " x "
        vertical_row2.append(" x ")
    elif play1 == 9:
        vertical_row3.append(" x ")
        diagonale1.append(" x ")
        row3[play1 // 2] = " x "

    plateau = ["".join(row1), '\n', mid_row1, '\n', ''.join(row2), '\n', mid_row1, '\n', ''.join(row3)]
    print(plateau)

    # vérifie si un user2 a gagné
    if row1.count(" x ") == 3 or row2.count(" x ") == 3 or row3.count(" x ") == 3 or diagonale1.count(" x ") == 3 or diagonale2.count(" x ") == 3 or vertical_row1.count(" x ") == 3 or vertical_row2.count(" x ") == 3 or vertical_row3.count(" x ") == 3:
        print("Bravo vous avez gagné ")
        exit()

    play2 = int(input("Que le second joueur joue son coup : "))

    # vérifie sur quelle ligne le coup de user2 est joué
    if play2 == 2:
        row1[play2] = " o "
        vertical_row2.append(' o ')
    elif play2 == 1:
        vertical_row1.append(' o ')
        diagonale1.append(' o ')
        row1[play2 - 1] = " o "
    elif play2 == 3:
        vertical_row3.append(' o ')
        diagonale2.append(' o ')
        row1[play2 + 1] = " o "
    if play2 == 4:
        vertical_row1.append(' o ')
        row2[play2 % 3 - 1] = " o "
    elif play2 == 5:
        diagonale1.append(' o ')
        diagonale2.append(' o ')
        vertical_row2.append(' o ')
        row2[play2 % 3] = " o "
    elif play2 == 6:
        vertical_row3.append(' o ')
        row2[play2 // 2 + 1] = " o "
    if play2 == 7:
        vertical_row1.append(' o ')
        diagonale2.append(' o ')
        row3[play2 % 3 - 1] = " o "
    elif play2 == 8:
        vertical_row2.append(' o ')
        row3[play2 % 3] = " o "
    elif play2 == 9:
        vertical_row3.append(' o ')
        diagonale1.append(' o ')
        row3[play2 // 2] = " o "

    print(plateau)
