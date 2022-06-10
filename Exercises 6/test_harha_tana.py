# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 10:16:18 2021

@author: fflattery
"""
from harha_tana import harha_tana_encipher_character

def test_harha_tana_encipher_character():
    assert harha_tana_encipher_character('a') == 'b'
    assert harha_tana_encipher_character('T') == 's'
    assert harha_tana_encipher_character(';') == ';'