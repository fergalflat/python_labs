# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 19:18:32 2021

@author: fflattery
"""

feet = float(input("Enter the number of feet: "))
inches = float(input("Enter the number of inches: "))


totalInches = (feet*12) + inches
totalInches2 = float(totalInches)
centimetres = totalInches2*2.54
metres = centimetres/100
metres = round(metres,4)

print("The distance in metres is: " + str(metres))