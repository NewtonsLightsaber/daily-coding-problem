'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

import math

# epsilon value to maintain precision
EPS = 1e-9

def get_new_arr(arr):
    '''
    Add in log space instead of multiplying => no division
    '''
    n = len(arr)
    new_arr = [0] * n
    zero_index = None
    has_many_zeros = False
    sum = 0

    for i in range(n):
        if arr[i] != 0:
            sum += math.log10(arr[i])

        elif zero_index is None: # First 0 found
            zero_index = i

        else: # More than 1 zeros
            has_many_zeros = True
            break

    if not has_many_zeros:
        if zero_index is not None:
            new_arr[zero_index] = int(EPS + pow(10, sum))

        else:
            for i in range(n):
                new_arr[i] = int(EPS + pow(10, sum - math.log10(arr[i])))

    return new_arr

assert get_new_arr([1,2,3,4,5]) == [120,60,40,30,24]
assert get_new_arr([3,2,1]) == [2,3,6]
assert get_new_arr([1,2,3,4,0]) == [0,0,0,0,24]
assert get_new_arr([1,0,3,4,0]) == [0,0,0,0,0]
