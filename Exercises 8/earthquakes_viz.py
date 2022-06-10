#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program to visualise Earthquake data from a csv file
Example of: Visualisation with Matplotlib

@author: cormac
"""
import datetime
from math import sqrt
import matplotlib.pyplot as plt

# the dictionary will contain
# as key: a tuple containing the time,latitude and longitude
# as value: the magnitude of the corresponding earthquake
earthquakes = {}

# open the file (deliberately leaving out exception handling)
with open("earthquakes_2019.csv") as data_file:
    _ = data_file.readline() # discard the headers
    
    for line in data_file:
        #split the line into 5 variables
        # maxsplit leaves the last column in a single variable
        # this avoids the complication of the place containing commas
        time_string, latitude, longitude, magnitude, place = line.split(",",maxsplit=4)
        
        when = datetime.datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S.%fZ")
        
        # insert into the dictionary
        earthquakes[when] = float(magnitude)


# visualisations
# Create the figure and axes
fig, ax = plt.subplots(1,3,figsize=(15,10))
# Set the title for the figure
fig.suptitle("Visualisations of Earthquake Manitude")
# 1 histogram    
# Set the title
ax[0].set_title("Histogram")
# set the axis labels
ax[0].set_xlabel("Magnitude")
ax[0].set_ylabel("Frequency")
# create a list for the histogram boundaries
bins_list = [i for i in range(0,10)]
# set the ticks on the x-axis
ax[0].set_xticks(bins_list)
# Display a histogram of the patient numbers
ax[0].hist(earthquakes.values(),bins = bins_list,ec="black")
# 2. Box plot
# Set the title
ax[1].set_title("Box Plot")
# set the y axis label
ax[1].set_ylabel("Magnitudes")
# Display a box plot of the patients numbers
ax[1].boxplot(earthquakes.values())
# 3. Violin plot 
# Set the title
ax[2].set_title("Violin Plot")
# set the y axis label
ax[2].set_ylabel("Patients")
# Display a box plot of the patients numbers
ax[2].violinplot(earthquakes.values(), showmedians=True)

#Inter-Quartile Range 25%
sort_data_25 = sorted(earthquakes.values())
index_25 = len(sort_data_25)*.25
rounded_25 = round(index_25)
sort_data_25[rounded_25]   
#Inter-Quartile Range 75%
sort_data_75 = sorted(earthquakes.values())
index_75 = len(sort_data_75)*.75
rounded_75 = round(index_75)
sort_data_75[rounded_75]  
#InterQuartile
IQR = (sort_data_75[rounded_75]) - (sort_data_25[rounded_25])
print(f"IQR: {IQR:.1f}")
    
#Mean
mean_height = sum(earthquakes.values())/len(earthquakes.values())
print(f"Mean: {mean_height:.1f}") # The average height of everyone in the list (6.55 feet!)

#Median
e_v = sorted(earthquakes.values())
mid_index = int(len(e_v)/2)
if len(e_v) %2 ==1:
    median = e_v[mid_index]
else:
    median = (e_v[mid_index - 1] + e_v[mid_index])/2
print("Median:", median)

#Mode
distinct_height = sorted(list(set(e_v)))   
frequencies = [e_v.count(magnitude) for magnitude in distinct_height ]
max_freq = max(frequencies)
max_index = frequencies.index(max_freq)
print("Mode:", distinct_height[max_index],)

#Standard Deviation
squared_deviations = [(magnitude - mean_height) ** 2 for magnitude in earthquakes.values()]
std_dev = sqrt(sum(squared_deviations)/(len(earthquakes.values())-1))
print(f"Standard Deviation: {std_dev:.2f}")


#Skewness
mode_skewness = (mean_height - (distinct_height[max_index]))/std_dev
median_skewness = 3*(mean_height - median)/std_dev

print(f"{mode_skewness=:.3f}")
print(f"{median_skewness=:.3f}")



