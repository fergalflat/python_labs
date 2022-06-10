# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 11:40:25 2021

@author: fflattery
"""

constituencies_list = []
seats_list = []

with open("constituencies.csv") as data_file:
    headers = data_file.readline()
    
    for line in data_file:
        Constituency, Seats = line.split(",")
        constituencies_list.append(Constituency)
        seats_list.append(int(Seats))
        
print("Number of constituencies:", len(constituencies_list))
print("Total number of seats:", sum(seats_list))
print(f"Mean number of seats per constituency: {sum(seats_list)/len(constituencies_list):.1f}")

#median
seats_list.sort()
mid_index = int(len(seats_list)/2)
if len(seats_list) & 2 == 1:
    median = seats_list[mid_index]
else:
    median = (seats_list[mid_index - 1] + seats_list[mid_index])/2
print(f"Median number of Seats: {median:.0f}")
print("")


#Type
frequency_3 = seats_list.count(3)
frequency_4 = seats_list.count(4)
frequency_5 = seats_list.count(5)

values = [3,4,5]
frequencies = (frequency_3, frequency_4, frequency_5)

print(f"{'Type':<8} Constituencies")
for num_seats,frequency in zip(values, frequencies):
    print(f"{num_seats}-Seater {frequency:>8}")


#Mode
#unique numbers
data = list(zip(values, frequencies))
num=(0, 0)
for item in data:
  if item[1]>num[1]:
    num=item
print(f"Most common constituency type: {num[0]}-Seater")  
