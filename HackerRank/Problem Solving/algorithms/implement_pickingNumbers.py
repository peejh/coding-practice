# https://www.hackerrank.com/challenges/picking-numbers

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()
    max_len = 0
    
    # mark indices of first occurrence of a number
    idx = [0,]
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            idx.append(i)
    idx.append(len(a))
    # print(idx)
    
    # calculate lengths of subarray with same number
    lens = []
    for i in range(1, len(idx)):
        lens.append(idx[i] - idx[i-1])
    # print(lens)
    
    # find max among subarrays of same number
    max_len = max(lens)

    # find max subarray length that meets condition
    for i in range(1, len(idx)-1):
        num1 = a[idx[i]]
        num2 = a[idx[i-1]]
        if abs(num1 - num2) < 2:
            max_len = max(max_len, lens[i] + lens[i-1])
    
    return max_len

def pickingNumbers_builtins(a):
    freqs = Counter(a)
    max_len = max(freqs.values())
    nums = list(sorted(freqs.keys()))

    for i in range(1, len(nums)):
        if abs(nums[i] - nums[i-1]) < 2:
            max_len = max(max_len, freqs[nums[i]] + freqs[nums[i-1]])

    return max_len

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()