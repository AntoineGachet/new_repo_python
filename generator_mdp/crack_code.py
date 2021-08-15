# créée tout les caractères puissant exister dans le mot de passe
caracteres_normaux = ["b", "c", "d", "e", "f",
                      "g", "h", "i", "j", "k",
                      "l", "m", "n", "o", "p",
                      "q", "r", "s", "t", "u", "v",
                      "w", "x", "y", "z", "a"]
caracteres_majuscules = ["A", "B", "C", "D", "E",
                         "F", "G", "H", "I", "J",
                         "K", "L", "M", "N", "O",
                         "P", "Q", "R", "S", "T",
                         "U", "V", "W", "X", "Y", "Z"]
caracteres_speciaux = ["[", "|", " ]", "@", "^", ":",
                       "/", "&", ";", ".", ",", "_",
                       "-", "!", "{", "}", "#"]
caracteres_nombre = ['1', '2', '3', '4', '5', '6', '7', '9', '8']


def crack_code(my_list1, my_list2, my_list3, my_list4, rep1, rep2, rep3, rep4):

    # demande à l'utilisateur quels type de carctères veut-il
    user_answer1 = rep1
    user_answer2 = rep2
    user_answer3 = rep3
    user_answer4 = rep4

    user_code = input("Entrez votre code ? ")

    # associe la réponse de l'utilisateur à la liste de caractère
    dico = {user_answer1: my_list1, user_answer2: my_list2,
            user_answer3: my_list3, user_answer4: my_list4}
    ma_liste = []

    # enlève les listes de caractères non demander par l'utilisateur
    # fusionne toute les listes ensemble en une seule non imbriquée
    if user_answer1 == "oui1":
        dico.pop(user_answer1)
        ma_liste.extend(my_list1)

    if user_answer2 == "oui2":
        dico.pop(user_answer2)
        ma_liste.extend(my_list2)

    if user_answer3 == "oui3":
        dico.pop(user_answer3)
        ma_liste.extend(my_list3)

    if user_answer4 == "oui4":
        dico.pop(user_answer4)
        ma_liste.extend(my_list4)

    # créer le mdp aléatoirement à partir de la liste créée précédemment
    # compare le mdp créée avec le vrai mdp
    mon_mdp = []
    user_code = list(user_code)

    for n in user_code:
        a = user_code.index(n)
        mon_mdp.append(user_code[a])
    print(''.join(mon_mdp))


crack_code(caracteres_normaux, caracteres_majuscules, caracteres_speciaux,
           caracteres_nombre, 'oui1', 'oui2', 'oui3', 'oui4')
