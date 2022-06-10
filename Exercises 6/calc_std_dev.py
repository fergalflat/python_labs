# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 10:59:33 2021

@author: fflattery
"""
from math import sqrt

def calc_standard_deviation(list_numbers):
    
    mean = sum(list_numbers)/len(list_numbers)

    squared_deviations = [(num - mean) ** 2 for num in list_numbers]
    std_dev = sqrt(sum(squared_deviations)/(len(list_numbers)-1))
    return std_dev
    
#if __name__ == "__main__":
   # print(f"{calc_standard_deviation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):.2f}")