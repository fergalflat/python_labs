# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 12:30:07 2021

@author: fflattery
"""
#Week2 Exercise 1
#input a mark and determine and display the corresponding award. Masters program grading
mark = int(input("Enter the overall mark: "))
if mark <0 or mark >100:
    print("Invalid input")
elif mark >= 70:
    print("First Class Honours")
elif 50 <= mark <= 69:
    print("Second Class Honours")
elif 40 <= mark <= 49:
    print("Pass")
else:
    print("No award")