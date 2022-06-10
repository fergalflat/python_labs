# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 20:36:13 2021

@author: fflattery
"""

import datetime

earthquakes = {}

with open ("earthquakes_2021.csv") as data_file:
    _ = data_file.readline()
    
    for line in data_file:
        time, latitude, longitude, depth, mag, = line.split(",")
        
        when = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")
        
        earthquakes[when] =  float(mag)
        
print("Number of earthquakes:", len(earthquakes))
print("Largest earthquake:", max(earthquakes, key=earthquakes.get), "with magnitude", max(earthquakes.values()))
print("Most recent earthquake:", max(earthquakes), "with magnitude", earthquakes.get(max(earthquakes)))
print("Least recent earthquake:",min(earthquakes), "with magnitude", earthquakes.get(min(earthquakes)))
print("Time difference:", max(earthquakes) - min(earthquakes))

#Most recent earthquake: 2021-11-09 19:48:30.960000 with magnitude 2.83
#Least recent earthquake: 2021-10-10 00:17:49.514000 with magnitude 3.3
#Time difference: 30 days, 19:30:41.446000