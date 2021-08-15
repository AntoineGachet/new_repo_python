import random
import json

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

# GENERATE THE USER'S CODE


def collage_liste(my_list1, my_list2, my_list3,
                  my_list4, rep1, rep2, rep3, rep4, rep5):

    # demande à l'utilisateur quels type de carctères veut-il
    user_answer1 = rep1
    user_answer2 = rep2
    user_answer3 = rep3
    user_answer4 = rep4
    user_answer5 = int(rep5)
    user_code = input('Pour quelle application créer ce mdp : ')

    # associe la réponse de l'utilisateur à la liste de caractère
    dico = {
        user_answer1: my_list1, user_answer2: my_list2,
        user_answer3: my_list3, user_answer4: my_list4
        }
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
    mon_mdp = []
    for i in range(user_answer5):
        x = random.randrange(len(ma_liste))
        mon_mdp.append(ma_liste[x])
    mdp = ''.join(mon_mdp)
    print(mdp)

    # put the password into json file
    Antoine_codes = "{0}: {1}".format(user_code, mdp)
    j = json.dumps(Antoine_codes)
    with open(r'C:\Users\antoi\OneDrive - Groupe Scolaire Montalembert\Bureau\python\Git\generator_mdp\modules\data_mdp.json', 'a+') as f:
        f.write(j)
        f.write(", ")

    mon_mdp = ''.join(mon_mdp)


collage_liste(caracteres_normaux, caracteres_majuscules,
              caracteres_speciaux, caracteres_nombre,
              'oui1', 'oui2', 'oui3', 'oui4', 12)

