import random

nombreTire=random.randint(0,100)
nombreTape=0

while nombreTape != nombreTire : 
      print("Tapez un nombre entier :")
      nombreTape = int(input())
      if nombreTape > nombreTire :
            print("c'est moins\n\n")

      elif nombreTape < nombreTire:
            print("c'est plus\n\n")

      else :
            print("c'est gagné")
    

