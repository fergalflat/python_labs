# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 18:37:09 2021

@author: fflattery
"""

irish_dict = {1:"A haon", 2:"A dó", 3:"A trí"}
#irish_dict.get(4)
#irish_dict.get(4, "Unknown")
irish_dict.keys()

import datetime




end_date = datetime.datetime.strptime("Mon Nov 08 09:00:00 GMT 2021", "%a %b %d %H:%M:%S %Z %Y")
end_date2 = datetime.datetime.strptime("Fri Dec 31 23:59:00 GMT 2021", "%a %b %d %H:%M:%S %Z %Y")

ans = end_date2 - end_date

time = datetime.datetime(2022, 1, 1, 0, 0, 0)
t2 = time + datetime(2022, 1, 9, 3, 4, 5)