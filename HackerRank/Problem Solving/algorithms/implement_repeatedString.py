# https://www.hackerrank.com/challenges/repeated-string
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # tracks the count of character 'a' in `s`
    count = 0 
    
    if n >= len(s):
        # Count the number of character 'a' in a single `s`
        count = sum([c == 'a' for c in s])
        # Multiply with the number of the full string `s`
        # that can fit in `n`
        count *= (n // len(s))
        # Set `n` to the remaining length after fitting
        # repeated full string `s` to `n`
        n %= len(s)
    
    # Count the number of character 'a'
    count += sum([c == 'a' for c in s[:n]])
    
    return count


def repeatedString_oneliner(s, n):
    return s.count('a') * (n // len(s)) + s[:n % len(s)].count('a')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()