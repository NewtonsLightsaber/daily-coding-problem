'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def has_pair_with_sum(arr, k):
    '''
    Check all pairs by 2 for loops, O(n log n) time
    '''
    n = len(arr)

    for i in range(n):
        remainder = k - arr[i]

        for j in range(i,n):
            if arr[j] == remainder:
                return True

    return False

def has_pair_with_sum_hash(arr, k):
    '''
    Hashing method, O(n) time
    '''

    # Empty hash set
    s = set()

    for i in range(len(arr)):
        remainder = k - arr[i]

        if remainder in s:
            return True

        s.add(arr[i])

    return False

assert has_pair_with_sum([10,15,3,7], 17) == True
assert has_pair_with_sum_hash([10,15,3,7], 17) == True
assert has_pair_with_sum_hash([17,15,3,0], 17) == True
