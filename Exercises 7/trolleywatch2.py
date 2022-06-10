import datetime

trolley_data = {}

with open("trolleywatch2.csv") as data_file:
    
    _ = data_file.readline()
    
    for line in data_file:
        
        date_string, Hospital, Region, Trolley, Ward, Patients = line.split(",")
    
        date_object = datetime.date.fromisoformat(date_string)
        
        if date_object not in trolley_data:
            trolley_data[date_object] = int(Patients)
        else:
            trolley_data[date_object] += int(Patients)
      
earliest = min(trolley_data)
latest = max(trolley_data)
difference =  (latest-earliest).days + 1


earliest = min(trolley_data).strftime('%d/%m/%Y')
latest = max(trolley_data).strftime('%d/%m/%Y')

 
print("Earliest date:", earliest)
print("Latest date:", latest)
print("Number of days:", difference)
print("Date with most patients:", max(trolley_data, key=trolley_data.get).strftime('%d/%m/%Y'))
print("Number of patients:", max(trolley_data.values()))