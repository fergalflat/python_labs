# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:46:38 2021

@author: fflattery
"""

from string import ascii_lowercase

text = input("Enter the text: ").lower()

frequencies = [0] * 26

for character in text:
    if character.isalpha():
        index = ascii_lowercase.find(character)
        
        frequencies[index +=1]
        
for i in range(26):
    print(f"")
