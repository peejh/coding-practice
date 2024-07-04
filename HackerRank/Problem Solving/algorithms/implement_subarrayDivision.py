# https://www.hackerrank.com/challenges/the-birthday-bar

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    '''
    s - integer array
    d - target sum
    m - number of addends
    '''
    
    running_total = sum([n for n in s[:m]])
    count = 1 if running_total == d else 0
    
    for i in range(m, len(s)):
        running_total += s[i] - s[i-m]
        if running_total == d:
            count += 1
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
