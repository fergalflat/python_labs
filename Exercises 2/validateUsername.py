# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 12:50:54 2021

@author: fflattery
"""

#Validata a username

username = str(input("Enter your username: "))

if 4 <= len(username) <= 8 and username[0].islower() and username.isalnum():
    print("Valid username")
else:
    print("Username is invalid:")
    
if len(username) <4:
    print("\tToo short - must have between 4 and 8 alphanumeric characters")
elif len(username) > 8:
    print("\tToo long - must have between 4 and 8 alphanumeric characters")
    
if not username[0].islower():   
    print("\tDoes not start with a lowercase letter")

if not username.isalnum():
    print("\tContains non-alphanumeric characters")

    
