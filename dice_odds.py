# -*- coding: utf-8 -*-
"""
@author: daniel ketterer
"""
from itertools import product
num_results = 3
min_number  = 4
num_dice    = 4
num_sides   = 8
possible_rolls = num_sides**num_dice


# make a hypercube of length num_sides and dimension num_dice  
temp = [list(range(1, num_sides+1)) for _ in range(num_dice)]
dice_rolls = list(product(*temp))

count  = 0
for roll in dice_rolls:
    count2 = 0
    for dice in roll:
        if (dice >= min_number):
            count2 = count2 + 1
        if(count2 >= num_results):
            count= count+1
            break
        
print(count/possible_rolls)
