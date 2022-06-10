# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:04:27 2021

@author: fflattery
"""

count = 0
while count < 3:
    username = input("Username: ")
    password = input("Password: ")

    if username == "aladdin" and password == "open_sesame":
        print("Login successful")
        break
    else:
        print("Incorrect username or password")
        count += 1

else:   
    print("Login failed")