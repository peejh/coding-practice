# https://www.hackerrank.com/challenges/larrys-array
# Source: MEDIUM

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    '''
    Solution is to count the number of inversions or swaps
    each element would require to get into its sorted place.
    The given array is sortable if the total number of
    inversions is divisible by 2.
    This is because every rotation requires 2 swaps, which
    means a sorted Larry's array would involve a number of
    swaps that is a multiple of 2.
    If the total number of inversions required is odd, then
    sorting Larry's array through rotations in sets of 3 is
    impossible.
    CONCEPT:
    https://en.wikipedia.org/wiki/Parity_of_a_permutation
    '''
    n = len(A)
    
    # To get the number of inversions required per element,
    # count the number of elements to its right that is lower
    # than it
    inversions = []
    for i in range(n-1):
        lower = 0
        for j in range(i+1, n):
            if A[j] < A[i]:
                lower += 1
        inversions.append(lower)
    
    # Evaluate if the total number of inversions is odd or even
    return 'NO' if sum(inversions) % 2 else 'YES'

def larrysArray_concise(A):
    parity = sum([A[i] > j for i in range(len(A)-1) for j in A[i+1:]]) % 2
    return ["YES", "NO"][parity]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
