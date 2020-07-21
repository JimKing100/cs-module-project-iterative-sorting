def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low_point = 0
    high_point = len(arr) - 1
    while low_point <= high_point:
        mid_point = (low_point + high_point) // 2
        guess = arr[mid_point]
        if guess == target:
            return mid_point
        if guess > target:
            high_point = mid_point - 1
        else:
            low_point = mid_point + 1
    return -1
