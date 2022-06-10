# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:41:19 2021

@author: fflattery
A substitution cipher is a simple encryption method which replaces each letter in the original message,
 called the plaintext, with another character in the enciphered (encrypted) message, called the ciphertext.  

For example, the Atbash cipher substitutes each letter with the corresponding one at the opposite end of the alphabet, 
i.e. a -> z, b->y, c->x, ... x->c, y->b, z->a.

Write and test a Python program which implements the Atbash cipher, as follows:

Input the plaintext from the user and convert it to lowercase
Create a variable to store the ciphertext, which should be initialised to an empty string ""
For each letter in the plaintext, find the corresponding letter at the opposite end of the alphabet and add this 
letter to the ciphertext; any character that is not a letter should be added on to the ciphertext as it is.
Display the ciphertext
Hint: Import the variable ascii_lowercase from the module string. It contains the letters of the alphabet "abcdef...xyz"

Only use the Python features that have been included at this point in the course.
"""
from string import ascii_lowercase

plaintext = input("Enter a message to encipher: ").lower()
ciphertext = ""
for character in plaintext:
     if character.isalpha():
          index = ascii_lowercase.find(character)
          ciphertext += ascii_lowercase[25-index
     else:
          ciphertext += character

print("The encrypted message is:", ciphertext)                