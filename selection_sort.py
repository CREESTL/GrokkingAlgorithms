'''
Сортировка выбором - это когда каждый выбранный элемент помещается в новый список
Здесь приведен пример сортировки массива по возрастанию сортировкой выбором.
O(n^2)
'''
import time
import random

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        # из исходного массива элемент удаляется
        new_arr.append(arr.pop(smallest))
    return new_arr

my_arr = [random.randint(1, 256) for i in range(100)]
start_time = time.time()
sorted_arr = selection_sort(my_arr)
end_time = time.time()
print(f"Sorting finished in {end_time - start_time:1.10f} seconds")
print(
