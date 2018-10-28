#examine each country’s name and population
#only in 2010
# population_data.json contains world population data from 1960 to 2010


import json 
filename = "population_data.json"

# Load the data into a list
with open(filename) as f:
    pop_data = json.load(f)

# Print the 2010 population for each country 
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        country_population = int(float(pop_dict["Value"]))
        print(country_name + " : " + str(country_population))