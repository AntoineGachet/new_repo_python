x=int
i=int(input('enter votre nombre de poule tué '))
o=int(input('enter votre nombre de chien tué '))
p=int(input('enter votre nombre de vache tué '))
u=int(input('enter votre nombre d''ami tué '))

def permis_chasse (y):
    x=i+3*o+5*p+10*u
    y=x*2
    return y
print(permis_chasse (x))