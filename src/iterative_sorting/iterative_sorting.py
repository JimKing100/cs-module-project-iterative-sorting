def selection_sort(arr):
    # Traverse throught the array
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # Find smallest element
        for j in range((cur_index + 1), len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # Swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


def bubble_sort(arr):
    # Traverse through the array
    for i in range(len(arr)-1):
        # Last i elements in place
        for j in range(0, len(arr)-i-1):
            # Traverse the array from 0 to length-i-1
            # Swap if element > next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Handle empty array
    if arr == []:
        return arr

    # Handle negative numbers
    for i in range(len(arr)):
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"

    # Handle the optional maximum argument
    if maximum is None:
        max_num = max(arr) + 1
    else:
        max_num = maximum + 1

    # Initialize the arrays
    size = len(arr)
    output = [0] * size
    count = [0] * max_num

    # Store the count of each element in count array
    for i in range(0, size):
        count[arr[i]] += 1

    # Store the cumulative count
    for i in range(1, max_num):
        count[i] += count[i - 1]

    # Find the index of each element of original array in count and put in output array
    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    return output
