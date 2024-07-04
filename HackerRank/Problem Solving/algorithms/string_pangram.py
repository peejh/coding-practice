# https://www.hackerrank.com/challenges/pangrams

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    letter_found = [False for _ in range(26)]
    s = s.lower()
    for c in s:
        if c.isalpha():
            letter_found[ord(c) - ord('a')] = True
    return 'pangram' if all(letter_found) else 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
