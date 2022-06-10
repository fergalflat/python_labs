from math import sqrt


countries_list = []
regions_list = []
gnps_list = []
birth_rates_list = []
life_exp_m_list = []
life_exp_f_list = []

try:
    with open("life.csv") as data_file:
        
        headings = data_file.readline()
        
        for line in data_file:
            try:
                country, region, gnp, birth_rate, life_exp_m, life_exp_f = line.split(",")
            except ValueError:
                print("Line has invalid format:", line)
                continue
            
            countries_list.append(country)
            regions_list.append(region)
            
            try:
                gnps_list.append(float(gnp))
            except ValueError:
                print(country, "has invalid GNP:", gnp)
                
            birth_rates_list.append(float(birth_rate))
            life_exp_m_list.append(float(life_exp_m))
            life_exp_f_list.append(float(life_exp_f))
            
    print()
    print()
    print("Results")
    print("Number of countries:", len(countries_list))
    distinct_regions = sorted(list(set(regions_list)))
    print("Number of distinct regions:", len(distinct_regions))
    print(f"Average number of countries per region: {len(countries_list)/len(distinct_regions):.2f}")      
    
    frequencies = [regions_list.count(region) for region in distinct_regions ]
    max_freq = max(frequencies)
    max_index = frequencies.index(max_freq)
    print("Region with the most countries (mode):", distinct_regions[max_index])
    mean_gnp = sum(gnps_list)/len(gnps_list)
    print(f"Mean GNP per country: {mean_gnp:.1f}")
    gnps_list.sort()
    mid_index = int(len(gnps_list)/2)
    
    if len(gnps_list) % 2 == 1:
        median = gnps_list[mid_index]
    else:
        median = (gnps_list[mid_index-1] + gnps_list[mid_index])/2
        
    print("Median GNP:", median)
    
    print("Range of GNPs (maximum - minimum):", max(gnps_list)-min(gnps_list))
    
    squared_deviations = [(gnp - mean_gnp) ** 2 for gnp in gnps_list]
    std_dev = sqrt(sum(squared_deviations)/(len(gnps_list)-1))
    print(f"Standard Deviation of GNPs: {std_dev:.2f}")
    
    x_mean = sum(birth_rates_list)/len(birth_rates_list)
    y_mean = sum(life_exp_f_list)/len(life_exp_f_list)
    z_mean = sum(life_exp_m_list)/len(life_exp_m_list)
    
    x_deviations = [x - x_mean for x in birth_rates_list]
    y_deviations = [y - y_mean for y in life_exp_f_list]
    z_deviations = [z - z_mean for z in life_exp_m_list]
    
    xy_deviations = [ x*y for (x,y) in  zip(x_deviations, y_deviations)]
    yz_deviations = [ y*z for (y,z) in zip(y_deviations, z_deviations)]
    
    x_squared_deviations = [(x - x_mean)**2 for x in birth_rates_list]
    y_squared_deviations = [(y - y_mean)**2 for y in life_exp_f_list] 
    z_squared_deviations = [(z-z_mean)**2 for z in life_exp_m_list]
                                                                      
    correlation = sum(xy_deviations)/sqrt(sum(x_squared_deviations)*sum(y_squared_deviations))
    print(f"The correlation between Female Life Expectancy (y) and Birth Rate (x): {correlation:.1f}")
    
    correlation2 = sum(yz_deviations)/sqrt(sum(z_squared_deviations)*sum(y_squared_deviations))
    print(f"Correlation between Female (y) and Male Life Expectancy (x): {correlation2:.1f}")
    
            
except (FileNotFoundError, PermissionError):
    print("Unable to open the file life.csv")                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
