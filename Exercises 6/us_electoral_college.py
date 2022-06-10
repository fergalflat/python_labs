from statistics_functions import calc_mean, calc_median, calc_mode, calc_standard_deviation, calc_correlation

state_list = []
population_list = []
electors_list = []

with open ("us_electoral_college.csv") as data_file:
    headers = data_file.readline()
        
    for line in data_file:
            
        State, Population, Electors = line.split(",")
            
        state_list.append(State)
        population_list.append(int(Population))
        electors_list.append(int(Electors))
        
    print(f"Number of States/Districts: {len(state_list)}")
    print()   
    print("Population")         
    print(f"Total: {sum(population_list):.0f}")
    print(f"Mean: {calc_mean(population_list):.1f}")
    print(f"Median: {calc_median(population_list):.1f}")
    print(f"Standard Deviation: {calc_standard_deviation(population_list):.1f}")
    print()
    print("Electors")            
    print(f"Total: {sum(electors_list):.0f}")
    print(f"Mean: {calc_mean(electors_list):.1f}")
    print(f"Median: {calc_median(electors_list):.1f}")
    print(f"Mode: {calc_mode(electors_list):.0f}")
    print(f"Standard Deviation: {calc_standard_deviation(electors_list):.1f}")
    print()
    print(f"Correlation between Electors and Population: {calc_correlation(electors_list, population_list):.1f}")