# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:29:02 2021

@author: fflattery
"""

from random import choice
quickpick =[]
all_numbers = list(range(1,48))

for i in range(6):
    
    number = choice(all_numbers)
    
    all_numbers.remove(number)
    
    quickpick.append(number)
    
quickpick.sort()

print("Your lotto numbers are:", quickpick)

