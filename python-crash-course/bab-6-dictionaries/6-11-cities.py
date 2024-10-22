#Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, 
# its approximate population, and one fact about that city. 
# The keys for each city’s dictionary should be something like country, population, and fact. 
# Print the name of each city and all of the information you have stored about it.

cities = {
    'jakarta' : { 
        'country' : 'Indonesia',
        'population' : '7 millon',
        'fact' : 'capital of Indonesia'
    },
    'amsterdam' : { 
        'country' : 'the Netherlands',
        'population' : '2 millon',
        'fact' : 'city and kanals'
    },
    'tokyo' : { 
        'country' : 'Japan',
        'population' : '10 millon',
        'fact' : 'Japanese capital city'
    }
}

for city, city_info in cities.items():
    print(f"{city.title()}")
    for info, detail in city_info.items():
        print(f"{info} : {detail}")
