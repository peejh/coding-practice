# https://www.hackerrank.com/challenges/funny-string

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    adj_diffs = [abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s) - 1)]
    low = 0
    high = len(adj_diffs) - 1
    while low < high:
        if adj_diffs[low] != adj_diffs[high]:
            return "Not Funny"
        low += 1
        high -= 1
    return "Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
