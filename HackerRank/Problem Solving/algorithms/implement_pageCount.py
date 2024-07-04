# https://www.hackerrank.com/challenges/drawing-book/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def pageCount(n, p):
    forward_flips = p // 2
    backward_flips = ((n if n % 2 else n+1) - p) // 2 # add 1 to n if even
      
    return min(forward_flips, backward_flips)    


def pageCount_bruteForce(n, p):
    forward_flips = 0
    backward_flips = 0
    
    start = 1
    while start < p:
        forward_flips += 1
        start += 2
    
    end = n - 1 if n % 2 else n
    while end > p:
        backward_flips += 1
        end -= 2
    
    return min(forward_flips, backward_flips)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
