#Write a function called city_country() that takes in the name of a city and its country. 
# The function should return a string formatted like this:

#“Santiago, Chile”

#Call your function with at least three city-country pairs, and print the value that’s returned.

def city_country(city, country):
    info = f"{city}, {country}"
    return info.title()

print(city_country("Santiago", "Chile"))
print(city_country("jakarta", "Indonesia"))
print(city_country("kuala lumpur", "malaysia"))
