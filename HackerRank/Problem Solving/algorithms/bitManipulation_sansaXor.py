# https://www.hackerrank.com/challenges/sansa-and-xor

#!/bin/python3

from itertools import combinations
from collections import defaultdict
from functools import reduce
import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sansaXor(arr):
    xors = defaultdict(int)

    for i, j in allSubArrays(arr):
        exist = xors[(i, j-1)]
        xors[(i, j)] = exist ^ arr[j-1]

    total = reduce(lambda acc, x: acc ^ x, xors.values())

    return total

def allSubArrays(arr):
    n = len(arr)
    indices = list(range(n + 1))

    for i, j in combinations(indices, 2):
        # yield arr[i:j]
        yield (i, j)

def sansaXor_best(arr):
    if len(arr) % 2 == 0:
        return 0
    
    total = 0

    for i in range(0, len(arr), 2):
        total ^= arr[i]
        
    return total

def sansaXor_best2(arr):
    if len(arr) % 2 == 0:
        return 0
    return reduce(lambda acc, x: acc ^ x, arr[::2], 0)        

def sansaXor_list(arr):
    '''
    uses list to store running XORs
    '''    
    total = 0
    stack = []
    
    for num in arr:
        for i in range(len(stack)):
            total ^= stack[i]
            stack[i] ^= num
        stack.append(num)
        
    for xor in stack:
        total ^= xor
    
    return total

def sansaXor_listInPlace(arr):
    '''
    same as above but stores the running XORs in the
    original array
    '''
    total = 0
    
    for i in range(len(arr)):
        for j in range(i):
            arr[j] ^= arr[i]
            total ^= arr[j]
        total ^= arr[i]
    
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
