# https://www.hackerrank.com/challenges/beautiful-pairs
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#

def beautifulPairs(A, B):
    '''
    The approach is to count the number of pairs that can
    be made per the given criteria, and then adding +1 to
    account for the element change that will be done on
    array `B`
    '''
    
    # Count pairs
    diff = Counter(B) - Counter(A)
    ans = len(B) - sum(diff.values())
    # Account for the element change in `B`
    # If everything is paired, subtract 1 instead of
    # adding 1 to account for the element change in `B`
    ans += 1 if diff else -1
        
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
