# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:01:30 2021

@author: fflattery
"""

import re

def validate_credit_card_number(number):
    if re.fullmatch("(?:\d{4}-){3}\d{4}", number):
        return True
    else:
        return False

