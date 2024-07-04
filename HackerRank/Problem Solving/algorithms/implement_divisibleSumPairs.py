# https://www.hackerrank.com/challenges/divisible-sum-pairs

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    '''
    > O(n) time and space complexity
    > this solution is similar to the two-sum problem where we store 
    information on a complement number for later access
    > here, we store mods of each number in the array with k, i.e.
    the remainders. this information is useful since we know how far 
    is each number to a multiple of k. notice that two remainders that
    add up to k is an answer. a 0 remainder paired with another 0
    remainder is also an answer.
    '''

    remainders = defaultdict(int) # use defaultdict to avoid KeyErrors

    for n in ar:
        remainders[n % k] += 1
        
    count = 0

    # iterate only up to k / 2 to avoid double counting of pairs
    for i in range((k // 2) + 1):
        # two 0 remainders are a valid pair
        # two k/2 remainders also make a valid pair
        if i == 0 or i * 2 == k:
            count += (remainders[i] * (remainders[i] - 1)) / 2 # (n(n-1))/2 formula
        else:
            count += remainders[i] * (remainders[k - i]) # pairing complements

    return int(count)

def divisibleSumPairs_bruteForce(n, k, ar):
    
    count = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
                
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()