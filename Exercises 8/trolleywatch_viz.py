#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program to visualise Trolley Watch data with a histrogram, box plot and violin plot
Example of: Visualisation with matplotlib
(For simplicity, ignoring errors, i.e. no Exception Handling)

"""
import matplotlib.pyplot as plt
from math import sqrt

# create a list for the patients numbers
patients_list = []

# read the data from the file
with open("trolleywatch.csv") as data_file:
    # read the first line containing the headings and discard it
    data_file.readline()
    
    # for each other line in the file
    for line in data_file:
        # split the line into the components
        date_string, hospital, region, trolley, ward, patients = line.strip().split(",")
        
        # add to the list
        patients_list.append(int(patients))

        
# Create the figure and axes
fig, ax = plt.subplots(1,3,figsize=(15,10))
# Set the title for the figure
fig.suptitle("Trolleywatch Visualisations")
# 1 histogram    
# Set the title
ax[0].set_title("Histogram of patient data")
# set the axis labels
ax[0].set_xlabel("Patients")
ax[0].set_ylabel("Frequency")
# create a list for the histogram boundaries
bins_list = [i for i in range(0,max(patients_list)+10,10)]
# set the ticks on the x-axis
ax[0].set_xticks(bins_list)
# Display a histogram of the patient numbers
ax[0].hist(patients_list, bins=bins_list,ec="black")
# 2. Box plot
# Set the title
ax[1].set_title("Box Plot of patient data")
# set the y axis label
ax[1].set_ylabel("Patients")
# Display a box plot of the patients numbers
ax[1].boxplot(patients_list)
# 3. Violin plot 
# Set the title
ax[2].set_title("Violin Plot of patient data")
# set the y axis label
ax[2].set_ylabel("Patients")
# Display a box plot of the patients numbers
ax[2].violinplot(patients_list, showmedians=True)

#Inter-Quartile Range 25%
sort_data_25 = sorted(patients_list)
index_25 = len(sort_data_25)*.25
rounded_25 = round(index_25)
sort_data_25[rounded_25]   
#Inter-Quartile Range 75%
sort_data_75 = sorted(patients_list)
index_75 = len(sort_data_75)*.75
rounded_75 = round(index_75)
sort_data_75[rounded_75]  
#InterQuartile
IQR = (sort_data_75[rounded_75]) - (sort_data_25[rounded_25])
print(f"IQR: {IQR:}")
    
#Mean
mean_height = sum(patients_list)/len(patients_list)
print(f"Mean: {mean_height:.1f}") # The average height of everyone in the list (6.55 feet!)

#Median
patients_list.sort()
mid_index = int(len(patients_list)/2)
if len(patients_list) %2 ==1:
    median = patients_list[mid_index]
else:
    median = (patients_list[mid_index - 1] + patients_list[mid_index])/2
print("Median:", median)

#Mode
distinct_height = sorted(list(set(patients_list)))   
frequencies = [patients_list.count(patients) for patients in distinct_height ]
max_freq = max(frequencies)
max_index = frequencies.index(max_freq)
print("Mode:", distinct_height[max_index],)

#Standard Deviation
squared_deviations = [(patients - mean_height) ** 2 for patients in patients_list]
std_dev = sqrt(sum(squared_deviations)/(len(patients_list)-1))
print(f"Standard Deviation: {std_dev:.2f}")


#Skewness
mode_skewness = (mean_height - (distinct_height[max_index]))/std_dev
median_skewness = 3*(mean_height - median)/std_dev

print(f"{mode_skewness=:.3f}")
print(f"{median_skewness=:.3f}")















