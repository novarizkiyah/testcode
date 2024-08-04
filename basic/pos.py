def get_positive_numbers(numbers):
    positive_numbers = []

    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
    return positive_numbers

numbers = [-10, 15, -3, 8, -1, 20, -7, 0, 5]
positive_numbers = get_positive_numbers(numbers)
print("Positive numbers:", positive_numbers)
