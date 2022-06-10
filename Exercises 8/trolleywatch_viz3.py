#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program to visualise Trolley Watch data 
Example of: Visualisation with matplotlib
(For simplicity, ignoring errors, i.e. no Exception Handling)
Version 2: get_data function returns a single dictionary
"""
import datetime


def get_data(filename):
    """
    Function to retrieve trolleywatch data from the file

    Parameters
    ----------
    filename : string
        The pathname of the file containing the data.

    Returns
    -------
    data : dict
        A dictionary containing as keys a tuple containing the date and hospital,
        and as values a tuple containing the region, trolley, ward and patient numbers
    """
    # create empty dictionary for the data
    data = {}
    
    # read the data from the file
    with open(filename) as datafile:
        # read the first line containing the headings and discard it
        datafile.readline()
        
        # for each other line in the file
        for line in datafile:
            # split the line into the components
            date_string, hospital, region, trolley, ward, patients = line.strip().split(",")
            
            # convert the date string to a datetime object
            date = datetime.date.fromisoformat(date_string)  
        
            # insert into dictionary 
            if (date,hospital) in data:
                print(line)
            data[(date,hospital)] = (region, int(trolley), int(ward), int(patients))

    return data
    
    
 # Main program   
if __name__ == "__main__":
    
    # get the data from the file
    data = get_data("trolleywatch3.csv")    
 
