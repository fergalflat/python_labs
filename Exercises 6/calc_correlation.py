# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 11:15:32 2021

@author: fflattery
"""
from math import sqrt

def calc_correlation(list_1, list_2):
    
    x_mean = sum(list_1)/len(list_1)
    y_mean = sum(list_2)/len(list_2)
    
    x_deviations = [x - x_mean for x in list_1]
    y_deviations = [y - y_mean for y in list_2]
    
    xy_deviations = [ x*y for (x,y) in  zip(x_deviations, y_deviations)]
    
    x_squared_deviations = [(x - x_mean)**2 for x in list_1]
    y_squared_deviations = [(y - y_mean)**2 for y in list_2]
    
    correlation = sum(xy_deviations)/sqrt(sum(x_squared_deviations)*sum(y_squared_deviations))
    return correlation

#if __name__ == "__main__":
    print(f"{calc_correlation([1, 2, 3, 4],[10, 20, 30, 40]):.3f}")

    print(f"{calc_correlation([1, 2, 3, 4],[10, 20, 30, 40]):.3f}")