# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:21:19 2021

@author: fflattery
"""

import re

with open("error.log") as logfile:
    contents = logfile.read()
    
    file_list = re.findall("File does not exist: ([\w/]+\.\w+)", contents)
    
    print("Number of missing file errors:", len(file_list))
    print("Number of unique missing fils:", len(set(file_list)))