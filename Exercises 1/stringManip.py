# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

fullname = input("Enter your first and last names, separated by a space: ")
temp = fullname.split()
print("Your username is: " + temp[0].lower() + temp[1][:1].lower())