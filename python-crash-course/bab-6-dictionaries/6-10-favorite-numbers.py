# Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.

favorite_places = {
    'nova': ['jogja', 'jakarta', 'paris'],
    'mew': ['solo', 'madiun', 'mekkah'],
    'rina': ['madinah', 'bern', 'osaka']
}

# Correct way to iterate over the dictionary
for name, places in favorite_places.items():  # Use .items() to get both key and value
    print(name)
