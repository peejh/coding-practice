# https://www.hackerrank.com/challenges/camelcase

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    word_count = 1
    for c in s:
        if c.isupper():
            word_count += 1
    return word_count
    # return sum([1 if c.isupper() else 0 for c in s]) + 1 # one-liner

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
