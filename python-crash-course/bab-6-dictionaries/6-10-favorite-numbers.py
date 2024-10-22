# Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.


favorite_numbers = {
    'nova' : [7, 9, 6],
    'yasmin' : [4, 5, 2],
    'rizki' : [2, 5],
    'giring' : [8, 4, 2],
    'maya' : [10, 1, 8]
}

for name, numbers in favorite_numbers.items():
    print(f"My name is {name}")
    print(f"My favorite number is")
    for number in numbers:
        print(f"{number}")