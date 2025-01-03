#Write a function called describe_city() that accepts the name of a city and its country. 
# The function should print a simple sentence, such as Reykjavik is in Iceland. 
# Give the parameter for the country a default value. 
# Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city, country='Iceland'):
    print(f"{city} is in {country}")

describe_city(city='Reykjavik')
describe_city('City A')
describe_city(city="Jakarta", country="Indonesia")
describe_city(city='Amsterdam', country='the Netherlands')