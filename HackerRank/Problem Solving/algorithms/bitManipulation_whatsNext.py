# https://www.hackerrank.com/challenges/whats-next

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatsNext' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def whatsNext(arr):
    
    if len(arr) == 1:
        arr[0] -= 1
        arr = [1, 1] + ([arr[0]] if arr[0] else [])
            
    elif len(arr) == 2:
        arr[0], arr[1] = arr[1] + 1, arr[0] - 1
        arr = [1, arr[0]] + ([arr[1]] if arr[1] else [])
            
    else: # if len(arr) >= 3
    
        if len(arr) % 2: # if odd
            arr[-1] -= 1
            arr[-2] -= 1
            
            if arr[-2]:
                arr = arr[:-1] + [1, 1, arr[-1]]
            else:
                arr[-3] += 1
                arr = arr[:-2] + [1, arr[-1]]
            
            if not arr[-1]:
                arr = arr[:-1]
        
        else: # if even
            if arr[-3] > 1 and arr[-2] > 1:
                arr[-3] -= 1
                arr[-2], arr[-1] = arr[-1] + 1, arr[-2] - 1
                arr = arr[:-2] + [1] + arr[-2:]
            elif arr[-3] == 1 and arr[-2] > 1:
                arr[-4] += 1
                arr[-2], arr[-1] = arr[-1] + 1, arr[-2] - 1
                arr = arr[:-3] + arr[-2:]
            elif arr[-3] > 1 and arr[-2] == 1:
                arr[-3] -= 1
                arr[-1] += 1
            else:
                arr[-4] += 1
                arr[-1] += 1
                arr = arr[:-3] + [arr[-1]]

    print(len(arr))
    print(*arr)

def whatsNext_wrong(arr):
    '''
    based on wrong assumption
    '''
    
    if len(arr) == 1:
        arr[0] -= 1
        if arr[0]:
            arr = [1, 1, *arr]
        else:
            arr = [1, 1]
            
    elif len(arr) == 2:
        arr[0] -= 1
        if arr[0]:
            arr = [1, 1, *arr]
        else:
            arr = [1, arr[1] + 1]
            
    else: # if len(arr) >= 3
    
        if len(arr) % 2: # if odd
            arr[-1] -= 1
            arr[-2] -= 1
            
            if arr[-2]:
                arr = arr[:-1] + [1, 1, arr[-1]]
            else:
                arr[-3] += 1
                arr = arr[:-2] + [1, arr[-1]]
            
            if not arr[-1]:
                arr = arr[:-1]
        
        else: # if even
            if arr[-3] > 1 and arr[-2] > 1:
                arr[-2] -= 1
                arr[-3] -= 1
                arr = arr[:-2] + [1, 1] + arr[-2:]
            elif arr[-3] == 1 and arr[-2] > 1:
                arr[-4] += 1
                arr[-2] -= 1
            elif arr[-3] > 1 and arr[-2] == 1:
                arr[-3] -= 1
                arr[-1] += 1
            else:
                arr[-4] += 1
                arr[-1] += 1
                arr = arr[:-3] + [arr[-1]]

    print(len(arr))
    print(*arr)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        whatsNext(arr)
