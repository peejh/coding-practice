# https://www.hackerrank.com/challenges/insertionsort2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort(n, arr):
    for i in range(1, n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
        print(*arr)

def insertion_sort(arr):
    '''
    this one exchanges space for the repeated swaps
    '''
    for i in range(1, len(arr)):
        j = i
        key = arr[i]
        while j > 0 and arr[j-1] > key:
           arr[j] = arr[j-1]
           j -= 1
        arr[j] = key

def insertionSort2(n, arr):
    '''
    this one just uses for loop
    '''
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j-1] < arr[j]:
                break
            arr[j-1], arr[j] = arr[j], arr[j-1]
        print(*arr)
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
