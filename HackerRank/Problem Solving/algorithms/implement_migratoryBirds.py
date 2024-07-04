# https://www.hackerrank.com/challenges/migratory-birds

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    '''
    O(n log n) time - because of sort
    O(1) space
    '''
    
    n = len(arr)
    sightings = -1
    bird_id = 0
    
    arr.sort()

    i = 0
    while i < n:
        curr_bird = arr[i]
        curr_sighting = 1

        while i+1 < n and arr[i] == arr[i+1]:
            curr_sighting += 1
            i += 1

        if curr_sighting > sightings:
            sightings = curr_sighting
            bird_id = curr_bird
            
        i += 1
    
    return bird_id

def migratoryBirds_withBuiltins(arr):
    '''
    O(n) time and space
    '''
    
    sightings = Counter(arr)
    max_sightings = max(sightings.values())
    bird_id = sys.maxsize
    
    for bird, sight in sightings.items():
        if sight == max_sightings and bird < bird_id:
            bird_id = bird
            
    return bird_id

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()