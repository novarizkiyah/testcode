#Write a function called city_country() that takes in the name of a city and its country. 
# The function should return a string formatted like this:

#“Santiago, Chile”

#Call your function with at least three city-country pairs, and print the value that’s returned.

def city_country(city, country):
    cities = f"{city}, {country}"
    return cities.title()


print(city_country("jakarta", "Indonesia"))
print(city_country("amsterdam", "the netherlands"))
print(city_country("kuala lumpur", "malaysia"))
