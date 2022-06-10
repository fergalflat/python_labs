# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 18:44:44 2021

@author: fflattery
"""

hogsheads = input("Enter the number of Hogsheads: ")
barrel = int(hogsheads)*2
temp = barrel*36
litres = temp*4.54609
litres  = round(litres,1)

print("Equivalent volume in litres is " +str(litres))