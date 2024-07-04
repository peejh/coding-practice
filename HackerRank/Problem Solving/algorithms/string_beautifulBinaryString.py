# https://www.hackerrank.com/challenges/beautiful-binary-string/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    if len(b) < 3:
        return 0
    
    b = list(b)
    mod_count = 0
    
    for i in range(len(b) - 2):
        curr = b[i:i+3]
        if ''.join(curr) == "010":
            b[i+2] = '1'
            mod_count += 1
    
    return mod_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
