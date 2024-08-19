# Input: Array 1: [1, 3, 5, 7, 9] Array 2: [2, 4, 6, 8, 10] 
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arr1=[1, 3, 5, 7, 9]
arr2=[2, 4, 6, 8, 10] 

def merge_sorted_arrays(arr1, arr2):
    result = []
    i = 0  # pointer for arr1
    j = 0  # pointer for arr2

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Add any remaining elements from arr1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    # Add any remaining elements from arr2
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

hasil=merge_sorted_arrays(arr1, arr2)
print(hasil)