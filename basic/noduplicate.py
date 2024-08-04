#Input: [1, 2, 3, 2, 4, 3, 5]
#Output: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 2, 4, 3, 5]

def no_duplicate(numbers):
    seen = set()
    new_number = []

    for number in numbers:
        if number not in seen:
            seen.add(number)
            new_number.append(number)
    return new_number

result134=no_duplicate(numbers)
print(result134)