# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 10:53:40 2021

@author: fflattery
"""

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
    
#if __name__ == "__main__":
  #  print(calc_mode([1,1,2,2,2,3, 3,3 ,3]))