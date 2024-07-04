# https://www.hackerrank.com/challenges/counting-valleys

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    valley_count = 0
    elevation = 0
    
    for step in path:
        prev = elevation
        elevation += 1 if step == 'U' else -1
        valley_count += 1 if prev == 0 and elevation == -1 else 0
            
    return valley_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
