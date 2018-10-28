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
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        country_population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code: 
            print(code + " : " + str(country_population))
        else:
            print("ERROR " + ": " + country_name)
        # print(country_name + " : " + str(country_population))

# Building our first americas map
world_map0 = pygal.maps.world.World()
world_map0.title = "North, Central and South America"
# North America
world_map0.add('North America', ['ca', 'mx', 'us'])
# Central America
world_map0.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# South America
world_map0.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf','gy', 'pe', 'py', 'sr', 'uy', 've'])
world_map0.render_to_file('americas.svg')

# Building our second americas map
world_map1 = pygal.maps.world.World()
world_map1.title = 'Populations of Countries in North America'
world_map1.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
world_map1.render_to_file('na_populations.svg')
