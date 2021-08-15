i=int(input('entrez botre nombre'))
r=2

if i//2%2==0:
    for r in range (2,i//2,2**i):
        print ('votre nopmbre est divisible par',r)

