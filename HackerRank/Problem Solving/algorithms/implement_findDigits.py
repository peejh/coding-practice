# https://www.hackerrank.com/challenges/find-digits
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    div_count = 0
    num = n
    
    while num > 0:
        d = num % 10
        if d and n % d == 0:
            div_count += 1
        num = num // 10
        
    return div_count

def findDigits_v2(n):
    div_count = 0
    
    for num in str(n):
        div = int(num)
        if div and n % div == 0:
            div_count += 1
        
    return div_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
