# https://www.hackerrank.com/challenges/strange-advertising
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    '''
    O(n) time
    O(1) space
    '''
    
    total = 0
    shares = 5
    for _ in range(n):
        likes = shares // 2
        total += likes
        shares = likes * 3

    return total

def viralAdvertising(n):
    '''
    O(n) time
    O(n) space
    '''
    
    likes = [2]
    for i in range(n-1):
        likes.append(likes[i] * 3 // 2)

    return sum(likes)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
