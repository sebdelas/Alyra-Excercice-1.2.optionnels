#!/usr/bin/env python3

from itertools import permutations

ordres = [
            [['Doge', 84],['LTC', 32],0.381],
            [['Doge', 29],['ETH', 80],2.75],
            [['ETH', 300],['BTC', 62],0.206],
            [['LTC', 288],['ETH', 2304],8],
            [['BTC', 27],['Doge', 46],1.7],
            [['BTC', 33],['LTC', 16],0.48],                                    
         ]

ordres_possibles = []
for i in range(3, len(ordres)+1):    
    for permutation in permutations(ordres, i):
        good_permutation = True
        #On élumine les combinaisons quand on obtient pas la même crypto à la fin que celle avec laquelle on a commencé
        if permutation[0][0][0] != permutation[-1][1][0]:
           continue
        for j in range(0,len(permutation)-1):
           #On élumine les combinaison quand les cryptos ne correspondent pas sur une transaction
           if permutation[j][1][0] != permutation[j+1][0][0]:
              good_permutation = False
              break
        if good_permutation:
           ordres_possibles.append(permutation)

for ordre in ordres_possibles:
   print(str(ordre))
