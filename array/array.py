

numbbers = [0, -2, -3, -5, 1, 3, 4, 6, 7, 5, 2, 14, 13, 45]

def find_max(numbbers):
    # Inisialisasi nilai maksimum dengan nilai elemen pertama dalam array
    max_number = numbbers[0]

    # Loop melalui setiap elemen dalam array
    for x in numbbers:
        # Jika elemen saat ini lebih besar dari max_number, perbarui max_number
        if x > max_number:
            max_number = x
    return max_number

result = find_max(numbbers)
print(result)

def find_min(numbbers):
    min_number=numbbers[0]

    for z in numbbers:
        if z < min_number:
            min_number = z
    return min_number

result2 = find_min(numbbers)
print(result2)


def count_positife(numbbers):
    count =numbbers[0]

    for x in numbbers:
        if x>0:
            count+=1
    return count

result3=count_positife(numbbers)
print(result3)

def count_even(numbbers):
    count1 = 0

    for a in numbbers:
        if a % 2 == 0:
            count1 += 1
    return count1
result4 = count_even(numbbers)
print(result4)

def find_max_index(numbbers):
    # Inisialisasi nilai maksimum dan indeksnya
    max_value=numbbers[0]
    max_index=0

    # Loop melalui setiap elemen dalam array dimulai dari indeks 1
    for i in range(1, len(numbbers)):
        if numbbers[i] > max_value:
            max_value = numbbers[i]
            max_index=i
    return max_index
result5=find_max_index(numbbers)
print(result5)