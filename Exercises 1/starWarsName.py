# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 18:34:54 2021

@author: fflattery
"""

firstname = input("Enter your firstname:")
lastname = input("Enter your lastname: ")
maidenname = input("Enter your mother's maiden name: ")
birthplace = input("Enter the name of your birthplace: ")

firstname = firstname[:3]
lastname = lastname[:2].lower()
maidenname = maidenname[:2]
birthplace = birthplace[:3].lower()

print("Your Star Wars name is: " + firstname + lastname + " " + maidenname + birthplace)
