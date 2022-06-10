# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:16:44 2021

@author: fflattery

Lotto List
"""
from random import randint
quickpick = []

while len(quickpick)<6:
    number = randint(1, 47)
    
    if number not in quickpick:
    
        quickpick.append(number)
    
quickpick.sort()

print("Your lotto numbers are:", quickpick)
    