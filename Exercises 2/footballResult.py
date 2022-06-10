# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:21:29 2021

@author: fflattery
"""

ht = str(input("Home team name: "))
hts = int(input("Home team score: "))
at = str(input("Away team name: "))
ats = int(input("Away team score: "))

if hts == ats:
    print("Draw")
elif hts > ats:
    print("Winner is", ht)
elif ats > hts:
    print("Winner is", at)
else:
    print("")