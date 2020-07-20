from iterative_sorting import selection_sort, counting_sort


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = [5, 4, 7]

results = selection_sort(arr1)
print(results)

results1 = counting_sort(arr1)
print(results1)

results2 = counting_sort(arr2)
print(results2)
