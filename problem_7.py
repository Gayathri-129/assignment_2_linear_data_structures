def move_negative_elements(array):
    j = 0
    for i in range(len(array)):
        if array[i] < 0:
            if j >= 0:
                array[j], array[i] = array[i], array[j]
            j += 1
    return array


array = [-4, 0, -1, 2, 3, -4, 5, -6, 7, 8, -9]
print(array)
print(move_negative_elements(array))