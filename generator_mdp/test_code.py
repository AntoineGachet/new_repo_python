
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


# TEST USER'S CODE

def test_code(ma_list1, ma_list2, ma_list3, ma_list4):
    user_code = input('entrez votre code : ')
    list(user_code)
    type_caractere = []

    for n in range(len(user_code)):
        for i in range(len(ma_list1)):
            if user_code[n] == ma_list1[i]:
                type_caractere.append(ma_list1)
    for n in range(len(user_code)):
        for i in range(len(ma_list2)):
            if user_code[n] == ma_list2[i]:
                type_caractere.append(ma_list2)
    for n in range(len(user_code)):
        for i in range(len(ma_list3)):
            if user_code[n] == ma_list3[i]:
                type_caractere.append(ma_list3)
    for n in range(len(user_code)):
        for i in range(len(ma_list4)):
            if user_code[n] == ma_list4[i]:
                type_caractere.append(ma_list4)
    b = (len(user_code))
    a = (len(type_caractere))+1
    c = a**b
    if c < 10**3:
        print('votre mdp est trop devinable: il y a', c, 'de possibilitées')
    if 10**3 < c < 10**6:
        print('votre mdp est très devinable: il y a', c, 'de possibilitées')
    if 10**6 < c < 10**8:
        print('votre mdp est quelque peu devinable: il y a', c,
              ' de possibilitées')
    if 10**8 < c < 10**10:
        print("votre mdp est impossible à deviner: il y a", c,
              ' de possibilitées')
    if c > 10**10:
        print('votre mdp est imprévisible: il y a', c,
              ' de possibilitées')


test_code(caracteres_normaux, caracteres_majuscules,
          caracteres_speciaux, caracteres_nombre)
