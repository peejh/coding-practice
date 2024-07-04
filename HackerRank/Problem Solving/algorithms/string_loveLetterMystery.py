# https://www.hackerrank.com/challenges/the-love-letter-mystery/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    operation_count = 0
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            operation_count += abs(ord(s[left]) - ord(s[right]))
        left += 1
        right -= 1
    return operation_count

def theLoveLetterMystery_oneLiner(s):
    return sum([abs(ord(s[i]) - ord(s[-1-i])) for i in range(len(s) // 2)])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
