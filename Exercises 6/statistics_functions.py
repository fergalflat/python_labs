# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 11:21:37 2021

@author: fflattery
"""
from math import sqrt

def calc_mean(list_numbers):
    '''
    Calcualte the mean of list of numbers

    Parameters
    ----------
    list_numbers : list
        list of numbers.

    Returns
    -------
    float
        mean of list of numbers.

    '''
    mean = sum(list_numbers)/len(list_numbers)
    return mean

def calc_median(list_numbers):
    
    '''
    calcualte the median

    Parameters
    ----------
    list_numbers : list
        list of numbers.

    Returns
    -------
    median: float
        the median

    '''
    
    list_numbers.sort()
    
    mid_index = int(len(list_numbers)/2)
    
    if len(list_numbers) %2 ==1:
        median = list_numbers[mid_index]
    else:
        median = (list_numbers[mid_index - 1] + list_numbers[mid_index])/2
    
    return median

def calc_mode(list_numbers):
    '''
    get the mode of a list of numbers

    Parameters
    ----------
    list_numbers : list
        list of numbers.

    Returns
    -------
    float
        mode of the numbers.

    '''
    distinct_numbers = sorted(list(set(list_numbers)))   
    frequencies = [list_numbers.count(num) for num in distinct_numbers ]
    max_freq = max(frequencies)
    max_index = frequencies.index(max_freq)
    
    return distinct_numbers[max_index]

def calc_standard_deviation(list_numbers):
    
    mean = sum(list_numbers)/len(list_numbers)

    squared_deviations = [(num - mean) ** 2 for num in list_numbers]
    std_dev = sqrt(sum(squared_deviations)/(len(list_numbers)-1))
    return std_dev

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