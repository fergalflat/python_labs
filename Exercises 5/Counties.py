# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:23:12 2021

@author: fflattery
"""
counties_list = []
wins_list = []
last_win_list = []
losses_list = []
last_loss_list = []
win_ratios_list = []

with open("hurling_finalists.csv") as data_file:
    headers = data_file.readline()
    
    
    for line in data_file:
        county, wins, last_win, losses, last_loss, win_ratio = line.split(",")
        counties_list.append(county)
        wins_list.append(int(wins))
        last_win_list.append(last_win)
        losses_list.append(int(losses))
        last_loss_list.append(last_loss)
        win_ratios_list.append(float(win_ratio.rstrip("%\n")))
        
print("Number of Counties:", len(counties_list))
print("Total number of All-Ireland finals:", sum(wins_list))
print(f"Average number of wins per county: {sum(wins_list)/len(counties_list):.1f}")
last_win_index = last_win_list.index("2021")
print("Current champions (winners in 2021):", counties_list[last_win_index])
max_wins = max(wins_list)
max_index = wins_list.index(max_wins)
print("Most wins:", counties_list[max_index], "with", max_wins, "wins, most recently in", last_win_list[max_index])
max_ratio = 100.0
percentage = max_ratio/100
percentage = "{0:.0%}".format(percentage)
max_ratio_index =  win_ratios_list.index(max_ratio)
print("Highest Win Ratio:", counties_list[max_ratio_index], "with", percentage +",","most recently in", last_win_list[max_ratio_index])

                