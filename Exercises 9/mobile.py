# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 15:56:17 2021

@author: fflattery
"""

import re

def validate_mobile_number(number):
    if re.fullmatch("^08[35679] \d{7}$", number):
        return True
    else:
        return False
    
if __name__ == "__main__":
   print(validate_mobile_number("086 4205256"))
        