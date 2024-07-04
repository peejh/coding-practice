# https://www.hackerrank.com/challenges/quicksort1/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    '''
    task is to only implement the partitioning
    '''
    pivot = arr[0]
    equal_count = 1
    lo, hi = 0, len(arr) - 1
    for num in arr[1:]:
        if num < pivot:
            arr[lo] = num
            lo += 1
        elif num > pivot:
            arr[hi] = num
            hi -= 1
        else:
            equal_count += 1
    for i in range(equal_count):
        arr[lo+i] = pivot
    return arr

def quickSort_recursive(arr):
    '''
    most readable version
    uses a random pivot
    '''
    if len(arr) < 2:
        return arr
        
    low, equal, high = [], [], []
    pivot = arr[random.randint(0, len(arr) - 1)]
    
    for num in arr:
        if num < pivot:
            low.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            high.append(num)
            
    return quickSort(low) + equal + quickSort(high)

def quickSort_noPivot(arr):
    '''
    pushes for a pivot towards the middle
    '''
    if len(arr) < 2:
        return arr
    
    lo, hi = 0, len(arr) - 1
    
    while lo != hi:
        while arr[lo] < arr[hi] and lo != hi:
            lo += 1
        arr[lo], arr[hi] = arr[hi], arr[lo]
        while arr[lo] < arr[hi] and lo != hi:
            hi -= 1
        arr[lo], arr[hi] = arr[hi], arr[lo]
        
    return quickSort_noPivot(arr[:lo]) + [arr[lo]] + quickSort_noPivot(arr[lo+1:])

def quickSort_inPlace(arr, left, right):
    '''
    uses constant space
    '''
    if left < right:
        pivot_idx = partition(arr, left, right)
        quickSort_inPlace(arr, left, pivot_idx-1)
        quickSort_inPlace(arr, pivot_idx, right)

def partition(arr, lo, hi):
    while lo != hi:
        while arr[lo] < arr[hi] and lo != hi:
            lo += 1
        arr[lo], arr[hi] = arr[hi], arr[lo]
        while arr[lo] < arr[hi] and lo != hi:
            hi -= 1
        arr[lo], arr[hi] = arr[hi], arr[lo]
    return lo

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
