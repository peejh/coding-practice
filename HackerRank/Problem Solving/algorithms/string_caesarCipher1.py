# https://www.hackerrank.com/challenges/caesar-cipher-1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    s = list(s)
    for i in range(len(s)):
        c = s[i]
        c = caesarEncrypt(c, k) if c.isalpha() else c
        s[i] = c
    return ''.join(s)

def caesarEncrypt(c, k):
    base = ord('a') if c.islower() else ord('A')
    return chr((ord(c) + (k % 26) - base) % 26 + base)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
