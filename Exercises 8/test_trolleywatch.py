# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:18:34 2021

@author: fflattery
"""

from trolleywatch_viz2 import get_data

def test_get_data():
    assert get_data("trolleywatch3.csv")