# -*- coding: utf-8 -*-
"""
Program to analyse data from life.csv
Example of: file input, exception handling and statistics
"""
import matplotlib.pyplot as plt

# create an empty list for each needed column
birthrates = []
male_life_exps = []
female_life_exps = []

# Try to open the file
try:
    with open("life.csv") as data_file:
        # read in the headers
        headers = data_file.readline()
        
        # for each line in the file
        for line in data_file:
            # try to process the line
            try:
                # split the line
                country, region, gnp, birthrate, male_life_exp, female_life_exp = line.split(",")
            except ValueError:
                # not enough values to split, or invalid value to convert
                print("Line has invalid format:", line)
                continue # continue to next line
                
            # append to the corresponding list, converting as necessary
            birthrates.append(float(birthrate))
            male_life_exps.append(float(male_life_exp))
            female_life_exps.append(float(female_life_exp))
            
    # add the visualisations here
    
#Scatterplot
    fig, ax = plt.subplots()
    ax.set_xlabel("Female Age")
    ax.set_ylabel("Male Age")
    ax.set_title("Male Life Expectancy v Female Life Expectancy")
    ax.scatter(female_life_exps, male_life_exps, marker=".")
    plt.show()    
    
    fig, ax = plt.subplots()
    ax.set_xlabel("Births per 1000")
    ax.set_ylabel("Female Age")
    ax.set_title("Female Life Expectancy v Birth Rate")
    ax.scatter(birthrates, female_life_exps, marker=".")
    plt.show() 
            
        

except FileNotFoundError:
    print("Unable to open file life.csv")
