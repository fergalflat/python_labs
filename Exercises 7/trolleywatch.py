# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 20:24:24 2021

@author: fflattery
"""

hospital_data = {}

with open("trolleywatch.csv") as data_file:
    
    _ = data_file.readline()
    
    for line in data_file:
        
        Date, Hospital, Region, Trolley, Wards, Patients = line.split(",")
        
        if Hospital not in hospital_data:
            
            hospital_data[Hospital] = int(Patients)
        else:
            hospital_data[Hospital] += int(Patients)
            
            
            
    print("Number of hospitals:", len(hospital_data))
    print("Hospital with most patients:", max(hospital_data, key=hospital_data.get) )
    print("Number of patients:", max(hospital_data.values()))