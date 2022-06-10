# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:48:52 2021

@author: fflattery

Getting infromation from a list
"""

values_string = input("Enter a series of numbers, separated by spaces: ")

numbers_list = [ int(i) for i in values_string.split() ]
#amount of numbers in the list
print("Number of values:", len(numbers_list))
print("Total:", sum(numbers_list))
print(f"Mean: {sum(numbers_list)/len(numbers_list):.1f}")
print("Maximum:", max(numbers_list))
print("Minimum:", min(numbers_list))

