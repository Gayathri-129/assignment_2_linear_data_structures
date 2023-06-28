import heapq


def find_kth_largest_smallest(array, k):
    kth_largest = heapq.nlargest(k, array)[-1]
    kth_smallest = heapq.nsmallest(k, array)[-1]
    return kth_largest, kth_smallest


# Example usage
arr = [9, 5, 2, 11, 8, 6]
k = 4

kth_largest, kth_smallest = find_kth_largest_smallest(arr, k)
print(f"{k}th largest element: {kth_largest}")
print(f"{k}th smallest element: {kth_smallest}")