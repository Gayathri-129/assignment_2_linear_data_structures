
def find_duplicates(array):
    seen = []
    duplicates = []
    for element in array:
        if element in seen:
            if element not in duplicates:
                duplicates.append(element)
        else:
            if element not in seen:
                seen.append(element)
    return duplicates


array = [1, 2, 1, 3, 4, 5, 0, 0, 1, 2, 3, 2]
duplicates = find_duplicates(array)

print(duplicates)