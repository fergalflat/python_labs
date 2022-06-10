# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:45:43 2021

@author: fflattery
"""
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

dates_data = {}
hospitals_data = {}
regions_data = {}

# create an empty list for the trolley and ward numbers
trolley_vs_ward_numbers = []

# read the data from the file
with open("trolleywatch3.csv") as datafile:
    # read the first line containing the headings and discard it
    datafile.readline()
    
    # for each other line in the file
    for line in datafile:
        # split the line into the components
        date_string, hospital, region, trolley, ward, patients = line.strip().split(",")
        
        # convert the date string to a datetime object
        date = datetime.date.fromisoformat(date_string)  

        # convert the patient value to an int, save having to code this repeatedly
        patients = int(patients)                          
        
        # if this is the first occurrence of this date
        if date not in dates_data:
            # insert into dictionary 
            dates_data[date] = patients
        else:
            dates_data[date] += patients

        # if this is the first occurrence of this hospital
        if hospital not in hospitals_data:
            # insert into dictionary 
            hospitals_data[hospital] = patients
        else:
            hospitals_data[hospital] += patients            

        # if this is the first occurrence of this region
        if region not in regions_data:
            # insert into dictionary 
            regions_data[region] = patients
        else:
            regions_data[region] += patients  
            
        # add the trolley and ward numbers to a list of tuples
        trolley_vs_ward_numbers.append((int(trolley),int(ward)))

# return the data structures for use with with matplotlib
#return dates_data, hospitals_data, regions_data, trolley_vs_ward_numbers


fig, ax = plt.subplots(2,2,figsize=(15,15))
ax[0,0].set_title("Pie Chart by Regions")
ax[0,0].pie(regions_data.values(), labels = regions_data.keys())

ax[0,1].set_title("Pie Chart by Regions")
y_pos = [i for i in range(len(hospitals_data))]
ax[0,1].set_yticks(y_pos)
ax[0,1].set_yticklabels(hospitals_data.keys())
ax[0,1].barh(y_pos, hospitals_data.values(), align="center")

ax[1,0].set_title("Date Plot")
ax[1,0].set_xlabel("Day")
ax[1,0].set_ylabel("Patients")
ax[1,0].xaxis.set_major_locator(mdates.DayLocator())
date_format = mdates.DateFormatter("%A")
ax[1,0].xaxis.set_major_formatter(date_format)
ax[1,0].plot_date(dates_data.keys(),dates_data.values() )

ax[1,1].set_title("Trolley vs Ward Numbers")
ax[1,1].set_xlabel("Trolleys")
ax[1,1].set_ylabel("Ward")
trolley_numbers = [ x[0] for x in trolley_vs_ward_numbers ]
ward_numbers = [ x[1] for x in trolley_vs_ward_numbers ]
ax[1,1].scatter(trolley_numbers, ward_numbers)








