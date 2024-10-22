# Use dictionary to store person you know
# store the first_name, last_name, age and the city.
# print each piece of information stored in your dictionaries

identity = {
    'first name' : 'nova',
    'last name' : 'rizkiyah',
    'age' : 31,
    'city' : 'rotterdam'
}


print(f"Hello, My name is {identity['first name'].title()} {identity['last name'].title()}")
print(f"I'm {identity['age']} years old")
print(f"I lived in {identity['city'].title()}")