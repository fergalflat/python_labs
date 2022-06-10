# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 20:09:38 2021

@author: fflattery
"""
import math

a = int(input("Enter semi-axis a: "))
b = int(input("Enter semi-axis b: "))

temp = math.sqrt((a*a)-(b*b))/a
print(temp)

temp3 = a*math.asin(temp)
print(temp3)

temp4 = temp3/temp
print(temp4)

temp5 = b + temp4
print(temp5)

temp6 = 2*math.pi*b
print(temp6)

temp7 = temp6*temp5
print(temp7)

print(f"The surface area is: {temp7:.2f}")
