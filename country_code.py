# this modules is meant to get the countries code
from pygal.maps.world import COUNTRIES


# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])

def get_country_code(country_name):
    """ Return Pygal's 2 digit country code for the given country's name"""
    for code, name in   COUNTRIES.items():
        if name == country_name:
            return code
    # if the country was not found return none
    return None

    # To test 
print(get_country_code('Afghanistan'))
