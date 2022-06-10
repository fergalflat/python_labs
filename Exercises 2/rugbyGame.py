# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:34:23 2021

@author: fflattery
"""

htname = str(input("Name of the home team: "))
htscore = int(input("Home team score: "))
httries = int(input("Number of tries scored by the home team: "))
atname = str(input("Name of the away team: "))
atscore = int(input("Away team score: "))
attries = int(input("Number of tries scored by the away team: "))

if (htscore > atscore) and (httries >= 4):
    print(htname,"awarded 5 championship points")
    
elif (htscore > atscore) and ( httries < 4):
    print(htname,"awarded 4 championship points")
    
elif (htscore < atscore) and ((atscore - htscore) <=7) and (httries >=4):
    print(htname,"awarded 2 championship points")
    
elif (htscore < atscore) and ( httries >=4):
    print(htname,"awarded 1 championship points")
    
elif (htscore < atscore) and ((atscore - htscore) <=7):
    print(htname,"awarded 1 championship points")
     
elif(htscore < atscore):
    print(htname,"awarded 0 championship points")
    
if (atscore > htscore) and (attries >= 4):
    print(atname,"awarded 5 championship points")
    
elif (atscore > htscore) and ( attries < 4):
    print(atname,"awarded 4 championship points")
    
elif (atscore < htscore) and ((htscore - atscore) <=7) and (attries >=4):
    print(atname,"awarded 2 championship points")
    
elif (atscore < htscore) and ( attries >=4):
    print(atname,"awarded 1 championship points")
    
elif (atscore < htscore) and ((htscore - atscore) <=7):
    print(atname,"awarded 1 championship points")
    
elif(atscore < htscore):
    print(atname,"awarded 0 championship points")
    
if (atscore == htscore) and httries >=4:
    print(htname,"awarded 3 championship points")
elif (atscore == htscore) and httries <4:
    print(htname,"awarded 2 championship points")
    
if (atscore == htscore) and attries >=4:
    print(atname,"awarded 3 championship points")
elif (atscore == htscore) and attries <4:
    print(atname,"awarded 2 championship points")
