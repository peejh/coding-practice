# https://www.hackerrank.com/challenges/append-and-delete
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):

    s_len = len(s)
    t_len = len(t)
    
    # Return YES if there is enough moves to fully
    # delete s and append t
    if s_len + t_len <= k:
        return 'Yes'
    
    # Find starting index where letters don't match
    i = 0
    while i < s_len and i < t_len and s[i] == t[i]:
        i += 1
    
    cost = s_len - i # delete
    cost += t_len - i if i < t_len else 0 # append
    leftover_burnable = (k - cost) % 2 == 0
        
    return 'Yes' if cost <= k and leftover_burnable else 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
