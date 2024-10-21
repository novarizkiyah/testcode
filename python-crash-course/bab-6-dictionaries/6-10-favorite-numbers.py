# Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.

favorite_numbers = {
    'nova': [1, 7, 6, 4],
    'mew': [5, 6, 1, 6, 3],
    'rina': [2, 5]
}

# Correct way to iterate over the dictionary
for name, numbers in favorite_numbers.items(): 
    print(f"My name is {name.title()} and my favorite number is")
    for number in numbers:
        print(f"\t {number}")
