a=int(input('enter your damn number'))
b=int(input('enter your damn number'))


def truc(c,d):
    if c%2==0:
        g=[]
        for i in range (c+1,d,2):
            g.append(i)
            
        return g
    else:
        g=[]
        for i in range(c,d,2):
            g.append(i)
        return g
        
print(truc(a,b))
