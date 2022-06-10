# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 10:02:02 2021

@author: fflattery
"""

from string import ascii_lowercase

def harha_tana_encipher_character(character):
    '''
    Encipher a character using harha tana

    Parameters
    ----------
    character : str
        The character to encipher.

    Returns
    -------
    str
        enciphered character.

    '''
    if not character.isalpha():
        return character
    else:
        index = ascii_lowercase.index(character.lower())
    
        if index % 2 == 0:
            new_index = index+1
        else:
            new_index = index-1
            
        return ascii_lowercase[new_index]
    