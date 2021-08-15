r=float(input('entrez un nombre'))
def factorielle(a) :
    if a == 0:
        return 1
    else:
        return a * factorielle(a-1)

print(factorielle(r))