# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 19:43:41 2021

@author: fflattery
"""
# Purpose of Program:  calculate the area and perimeter of a rectangular room and display them to 1 decimal place


length = float(input("Enter the length in metres: "))
width = float(input("Enter the width in metres: "))

area = length*width
perimeter = 2*(length + width)

area = round(area,1)
perimeter = round(perimeter,1)

print("The area is " + str(area) + " square metres")
print("The perimeter is " + str(perimeter) + " metres")