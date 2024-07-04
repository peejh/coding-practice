# https://www.hackerrank.com/challenges/big-sorting

#!/bin/python3

from functools import cmp_to_key
import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    def cmp_numeric_strings(s1, s2):
        # compare by length
        if len(s1) < len(s2):
            return -1
        elif len(s1) > len(s2):
            return 1
        # compare by ascii
        else:
            if s1 < s2:
                return -1
            elif s1 > s2:
                return 1
            else:
                return 0
            
    return sorted(unsorted, key=cmp_to_key(cmp_numeric_strings))
    
def bigSorting_best(unsorted):
    return sorted(unsorted, key=lambda s: (len(s), s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
