numbers = [-10, 15, -3, 8, -1, 20, -7, 0, 5]

def pos_number(numbers):
    simpan_number = []

    for number in numbers:
        if number>0:
            simpan_number.append(number)
    return simpan_number

result12 = pos_number(numbers)
print(result12)