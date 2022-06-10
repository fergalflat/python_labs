# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:01:40 2021

@author: fflattery
"""

year = int(input("Enter the year: "))
if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):   
    print("Leap Year");  
  # Else it is not a leap year  
else:
    print ("Not a Leap Year")