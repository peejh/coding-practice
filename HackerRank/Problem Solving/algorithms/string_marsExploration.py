# https://www.hackerrank.com/challenges/mars-exploration

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    original = "SOS"
    err_count = 0
    for i in range(len(s)):
        err_count += 1 if s[i] != original[i % 3] else 0
    return err_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
