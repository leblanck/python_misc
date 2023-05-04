'''bubble_sort.py'''
import random

def bubble_sort(arr: list):
    '''sort those bubble'''

    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j +1]:
                # Swap
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
    return arr

big_list = [random.randint(0, 999) for iter in range(1000)]
final_sort = bubble_sort(big_list)
print(final_sort)
