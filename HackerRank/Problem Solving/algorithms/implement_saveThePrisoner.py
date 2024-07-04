# https://www.hackerrank.com/challenges/save-the-prisoner
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

def saveThePrisoner(n, m, s):
    '''
    n - number of students
    m - number of candy to be distributed
    s - chair number where distribution starts
    '''
    
    m %= n
    ans = s + m - 1
    
    if ans <= n:
        if ans == 0: # happens when m=0, s=1
            return n
        return ans
    return ans - n

def saveThePrisoner_better(n, m, s):
    seatNo = (s + m - 1) % n
    return n if seatNo == 0 else seatNo

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
