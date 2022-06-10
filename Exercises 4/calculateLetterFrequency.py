# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:31:54 2021

@author: fflattery

Calculate letter frequencies
"""

from string import ascii_lowercase

text = input("Enter the text: ").lower()

frequencies = [0] * 26

for character in text:
    if character.isalpha():
        index = ascii_lowercase.find(character)
        frequencies[index]  += 1
        
print("\nLetter Frequency")
for i in range(26):
    print(f"   {ascii_lowercase[i]:<3} {frequencies[i]:>5}")
    
max_frequency = max(frequencies)
max_index = frequencies.index(max_frequency)

print("\nMost frequent letter:", ascii_lowercase[max_index])
