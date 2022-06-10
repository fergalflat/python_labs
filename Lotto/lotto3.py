# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:33:01 2021

@author: fflattery
"""

from random import shuffle

all_numbers = list(range(1, 48))

shuffle (all_numbers)

quickpick = all_numbers[:6]

quickpick.sort()

print("Your lotto numbers are:", quickpick)