# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:11:58 2021

@author: fflattery

A variable name can only consist of letters, numbers (digits) and the underscore character _.

Write and test a program which inputs a variable and displays a message indicating whether or not it is valid.

One possible approach is as follows:

Input the variable name
For each character in the variable name
    If the character is not valid
        Display "Variable name has invalid character" and display the character
        Break from the loop
If the loop completed (i.e. all characters were processed)
    Display "Valid variable name"
For example:
"""
var_name = input("Enter the variable name: ")

for character in var_name:
    if not character.isalnum() and character != "_":
        print("Invalid character", character)
        break
    
else: 
    print("Valid variable name")
