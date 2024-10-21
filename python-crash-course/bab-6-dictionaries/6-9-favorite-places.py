# Make a dictionary called favorite_places. 
# Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
# To make this exericse a bit more interesting, ask some friends to name a few of their favorite places. 
# Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places = {
    'nova': ['jogja', 'jakarta', 'paris'],
    'mew': ['solo', 'madiun', 'mekkah'],
    'rina': ['madinah', 'bern', 'osaka']
}

for name, places in favorite_places.items():
    print(f"My name is {name.title()} is ")
    for place in places:
        print(f"{place}")


