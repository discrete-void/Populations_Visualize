#examine each country’s name and population
#only in 2010
# population_data.json contains world population data from 1960 to 2010


# from country_codes import get_country_codes 
import json
import pygal 
from country_code import get_country_code
filename = "population_data.json"

# Load the data into a list
with open(filename) as f:
    pop_data = json.load(f)

# Print the 2010 population for each country 
# Plotting a complete Population map
# Firstly building a dictionary of population data
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        country_population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code: 
            # print(code + " : " + str(country_population))
            cc_populations[code] = country_population
# In order to make the maps visually acceptable, we are going to group the map into three categores below
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
# See how many countries are in each level
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
        

# # Building our first americas map
# world_map0 = pygal.maps.world.World()
# world_map0.title = "North, Central and South America"
# # North America
# world_map0.add('North America', ['ca', 'mx', 'us'])
# # Central America
# world_map0.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# # South America
# world_map0.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf','gy', 'pe', 'py', 'sr', 'uy', 've'])
# world_map0.render_to_file('americas.svg')

# # Building our second americas map
# world_map1 = pygal.maps.world.World()
# world_map1.title = 'Populations of Countries in North America'
# world_map1.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
# world_map1.render_to_file('na_populations.svg')


# world_map3 = pygal.maps.world.World()
# world_map3.title = 'World Population in 2010, by Country'
# world_map3.add('2010', cc_populations)
# world_map3.render_to_file('world_population.svg')


# Now we build our final world population map
final_world_map = pygal.maps.world.World()
final_world_map.title = "World Population as at 2010 categorised by countries"
final_world_map.add('0-10m', cc_pops_1)
final_world_map.add('10m-1bn', cc_pops_2)
final_world_map.add('>1bn', cc_pops_3)
final_world_map.render_to_file('categorised_world_population.svg')
