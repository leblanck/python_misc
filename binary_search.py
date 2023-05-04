'''Binary Search Basic'''

import math
import random

def binary_search(stack: list, needle: int) -> bool:
    '''Binary Search'''
    stack.sort()
    high = len(stack)
    low = 0

    while low < high:
        mid = math.floor(low + (high - low) /2)
        value = stack[mid]
        if value == needle:
            return True
        if value > needle:
            high = mid
        else:
            low = mid + 1

    return False

big_list = [random.randint(0, 99999) for iter in range(100000)]
found_object = binary_search(big_list, 3461)
print(found_object)
