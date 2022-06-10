# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 20:00:21 2021

@author: fflattery
"""

# Purpose of Program: input the length of a pendulum and then calculate the period and display the output formatted to 2 decimal places.
# Student ID: A00291231

from math import pi, sqrt

l = float(input("Enter the length of the pendulum: "))

g =float(9.81)

period = 2*pi*sqrt(l/g)

print("Period of the pendulum is", round(period,2), "seconds")
