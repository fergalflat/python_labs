# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:41:02 2021

@author: fflattery
"""

import re

with open("access.log") as logfile:
    contents = logfile.read()
    
    file_list = re.findall("(?<=\" )\d{3}", contents)
    
    distinct_regions = sorted(list(set(file_list)))
    
    frequencies = [file_list.count(region) for region in distinct_regions ]
    max_freq = max(frequencies)
    max_index = frequencies.index(max_freq)
    index = 0
    print("Code Frequency")
    print(distinct_regions[0],"  ", frequencies[0])
    print(distinct_regions[1],"   ", frequencies[1])
    print(distinct_regions[2],"    ", frequencies[2])
    print(distinct_regions[3],"    ", frequencies[3])
    print(distinct_regions[4],"   ", frequencies[4])
    print(distinct_regions[5],"     ", frequencies[5])
   # for code in distinct_regions:
    #    print(code, "  ", frequencies[index], flush=True )
     #   index = index+1
     