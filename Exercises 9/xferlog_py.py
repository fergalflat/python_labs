# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 19:56:02 2021

@author: fflattery
"""
import datetime
import re

date_list = []

with open("xferlog") as logfile:
    contents = logfile.read()
    
    file_list = re.findall("(?:\w{3})\ \d{2} \d{2}\:\d{2}\:\d{2} \d{4}", contents)
    
    for line in file_list:
    
        time = datetime.datetime.strptime(line, "%b %d %H:%M:%S %Y")#
        date_object = time.date()
        
        date_list.append(date_object)
        
    distinct_dates = sorted(list(set(date_list)))
    
    file_list2 = re.findall("\w+(?=\s+/)", contents)
    file_list2 = list(map(int, file_list2))
        
d = {}
k = list(zip(date_list, file_list2))
for (x,y) in k:
    if x in d:
        d[x] = d[x] + y 
    else:
        d[x] = y

print("Date       Amount Transferred (Bytes)")
for key, value in d.items():
    print(f"{key} {value:>15}")