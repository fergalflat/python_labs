# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 22:53:48 2021

@author: fflattery
"""

import datetime
import re

date_list = []

with open("nba2k20_players.csv") as logfile:
    _ = logfile.readline()
    contents = logfile.read()
    
    file_list = re.findall("^(?:[^,]*\,){4}([^,]*)", contents)
    
    for line in file_list:
    
        time = datetime.datetime.strptime(line, "%m/%d/%Y")#
        date_object = time.date()
        
        date_list.append(date_object)
        
    distinct_dates = sorted(list(set(date_list)))
    
    file_list2 = re.findall("^(?:[^,]*\,){5}([^,]*)", contents)
    file_list2 = list(map(int, file_list2))
        
d = {}
k = list(zip(date_list, file_list2))
for (x,y) in k:
    if x in d:
        d[x] = d[x] + y 
    else:
        d[x] = y

