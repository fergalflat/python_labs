# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 09:44:48 2021

@author: fflattery
"""
from wave_velocity import calc_wave_velocity
from pytest import approx

def test_calc_wave_velocity():
    assert calc_wave_velocity(0.5, 1, 1.1, 2) == approx(3.82, 0.01)
