#!/usr/bin/env python3

def calcul_factoriel(nb, puissance_de_deux):
   if (nb%2 == 0):
      first_impair = nb - 1
   else:
      first_impair = nb
   multi = 1
   for i in range(3, first_impair+1, 2):
      multi =  multi * i
   nb_div_deux = nb // 2
   puissance_de_deux = puissance_de_deux + nb_div_deux
   if (nb_div_deux > 1):
      return multi * calcul_factoriel(nb_div_deux, puissance_de_deux)      
   else:
      return multi * (2 ** puissance_de_deux)

nb = int(input("Saisissez un nombre : "))
factoriel = 1
factoriel = factoriel * calcul_factoriel(nb, 0)
print ("La factoriel de " + str(nb) +  " est " + str(factoriel))
