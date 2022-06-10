# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:55:12 2021

@author: fflattery
"""

username = input("Username: ")
password = input("Password: ")

while username != "aladdin" or password != "open_sesame":
    print("Incorrect username or password")
    
    username = input("Username: ")
    password = input("Password: ")
    
print("Login successful")