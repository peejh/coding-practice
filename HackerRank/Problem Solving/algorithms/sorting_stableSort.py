# https://www.hackerrank.com/challenges/countingsort4

#!/bin/python3

from functools import reduce
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # modify first half of arr
    for i in range(len(arr) // 2):
        arr[i][1] = '-'
    
    # find max key
    max_key = max([int(k) for k, _ in arr])
    
    # sort by keys and store in a dictionary
    ordered = [[] for _ in range(max_key + 1)]
    for k, v in arr:
        k = int(k)
        ordered[k].append(v)
    
    # display
    out = list()
    for item in ordered:
        out.extend(item)
    print(*out)

def countSort2(arr):
    '''
    built-in sort method is stable
    '''
    for i in range(len(arr)//2):
        arr[i][1] = '-'
    arr.sort(key=lambda x: int(x[0]))
    print(*[x[1] for x in arr])

if __name__ == '__main__':
    n = int(input().strip())

    arr = [] 

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
