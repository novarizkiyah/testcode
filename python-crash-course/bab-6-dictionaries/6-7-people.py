# Start with the program you wrote for Exercise 6-1 (page 98). 
# Make two new dictionaries representing different people, 
# and store all three dictionaries in a list called peoples. 
# Loop through your list of people. As you loop through the list, 
# print everything you know about each person.

identity_1 = {
    'first name' : 'nova',
    'last name' : 'rizkiyah',
    'age' : 31,
    'city' : 'rotterdam'
}
identity_2 = {
    'first name' : 'yamin',
    'last name' : 'moe',
    'age' : 21,
    'city' : 'sydney'
}
identity_3 = {
    'first name' : 'kala',
    'last name' : 'mahla',
    'age' : 11,
    'city' : 'jakarta'
}

peoples = [identity_1, identity_2, identity_3]

for ppl in peoples:
    print(
        f"Name : {ppl['first name'].title()} {ppl['last name'].title()}"
        f"\n Age : {ppl['age']} years old"
        f"\n Live in {ppl['city']}"
    )