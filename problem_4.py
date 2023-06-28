def count_pairs_with_sum(array, sum):
    count = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == sum:
                count += 1

    return count


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 10

count = count_pairs_with_sum(array, sum)

print(count)