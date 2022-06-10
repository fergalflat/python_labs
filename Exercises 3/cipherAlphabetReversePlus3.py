# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:06:36 2021

@author: fflattery
Write a program which inputs a plaintext message, enciphers it using the Caesar Cipher, and then displays the ciphertext.

The logic is as follows:

Input the plaintext

Convert the plaintext to lowercase

Take each character in the plaintext one at a time

If the character is a letter

Convert it into a number representing its position in the lowercase alphabet

Add 3 to this number, modulo 26 (this deals with the letters at the end of the alphabet)

Find the letter corresponding to this number in the UPPERCASE alphabet and add it to the ciphertext

Otherwise add the character on to the ciphertext exactly as it is

Display the ciphertext
"""
from string import ascii_lowercase

plaintext = input("Enter the message: ").lower()
ciphertext = ""
for character in plaintext:
     if character.isalpha():
          index = ascii_lowercase.find(character)
          
          ciphertext += ascii_lowercase[(index+3) % 26]
     else:
          ciphertext += character

print("The enciphered message is:", ciphertext.upper())                


