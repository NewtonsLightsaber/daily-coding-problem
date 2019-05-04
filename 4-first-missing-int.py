'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def first_missing_int(l):
    '''
    Explanation at https://stackoverflow.com/questions/51346136/given-an-array-of-integers-find-the-first-missing-positive-integer-in-linear-ti

    1 - Partition: rearrange array into 2 halves - 1st half non negative, 2nd half negative.
        Let 'end' be ending index of non negative first half e.g. [1, 2, 3, -2, -3] has end = 3
    2 - First pass: traverse for i = 0 : end, take abs val of l[i].
        If val > end, do nothing. Else, make l[val - 1] negative.
        Basically, we change the value of the element having index i to negative if i+1 is in the array.
        E.g. after step 2, l[2] negative => 3 is in array (and is not the answer)
    3 - Second pass: again traverse from 0-end.
        If l[i] >= 0 return i+1 (because this implies i+1 is not in the array).
        Else, return end+1.
    '''
    n = len(l)

    # 1 - Partition in positive half and negative half
    for i in range(n):
        if l[i] < 0:
            for j in range(i + 1, n):
                if l[j] >= 0:
                    l[i], l[j] = l[j], l[i]
                    break

                elif j == n - 1:
                    end = i - 1
                    break

    # 2 - Traverse from 0 to end, make value negative if value <= end
    for i in range(end):
        val = abs(l[i])
        if val <= end:
            l[val - 1] = -abs(l[val - 1])

    # 3 - Return lowest positiv integer not in array
    for i in range(end):
        if l[i] >= 0:
            return i + 1

    return end + 1

assert first_missing_int([1, -1, -5, -3, 3, 4, 2, 8]) == 5
assert first_missing_int([1, -1, -5, -3, 3, 4, 2, 0]) == 5
assert first_missing_int([1, -1, -5, -3, 3, 4, 2, 2]) == 5
