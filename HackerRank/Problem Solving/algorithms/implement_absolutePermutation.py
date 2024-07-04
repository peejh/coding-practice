# https://www.hackerrank.com/challenges/absolute-permutation
# Difficulty: MEDIUM

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    '''
    Absolute permutations, as described by the problem, is achieved
    by partitioning the sorted n elements into chunks of 2*k sizes.
    Each 2*k partition has the first half as its second, and its
    second half the first.
    e.g.    n=8, k=2    1 2 3 4 5 6 7 8 -> 3 4 1 2 7 8 5 6
    '''
    
    if k == 0:
        return list(range(1, n+1))
    
    # n must be divisible by 2*k
    if n % (2 * k) != 0:
        return [-1]
    
    ans = []
    modifier = 1
    
    for i in range(1, n+1, k):
        start = i + k * modifier
        # ans += list(range(start, start+k))
        ans += [j for j in range(start, start+k)]
        modifier *= -1

    # another take
    # for i in range(1, n+1, 2*k):
    #     ans.extend(range(i+k, i+2*k))
    #     ans.extend(range(i, i+k))

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
