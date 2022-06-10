# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 15:43:46 2021

@author: fflattery
"""

import re

def validate_athlone_landline_number(number):
    if re.fullmatch("^09064\d{5}$", number):
        return True
    else:
        return False
    
        
        