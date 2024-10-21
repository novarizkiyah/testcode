# Start with the program you wrote for Exercise 6-1 (page 98). 
# Make two new dictionaries representing different people, 
# and store all three dictionaries in a list called people. 
# Loop through your list of people. As you loop through the list, 
# print everything you know about each person.

identities_1 = {
    'first name' : 'nova',
    'last name' : 'rizkiyah',
    'age' : 31,
    'city' : 'rotterdam'
}

identities_2 = {
    'first name' : 'wanda',
    'last name' : 'kyaira',
    'age' : 2,
    'city' : 'paris'
}

identities_3 = {
    'first name' : 'nina',
    'last name' : 'herna',
    'age' : 3,
    'city' : 'london'
}

peoples = [identities_1, identities_2, identities_3]

for people in peoples:
    print(people)

for ppl in peoples:
    print(
        f"My first name is {ppl['first name'].title()}, ",
        f"my last name is {ppl['last name'].title()}, ",
        f"my age is {ppl['age']} years, ", 
        f"I live in {ppl['city'].title()}"
        )

