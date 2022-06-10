# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 10:37:48 2021

@author: fflattery
"""

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

#if __name__ == "__main__":
 #   print(calc_median([1,2,3,4]))
        