# https://www.hackerrank.com/challenges/strong-password

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    special_characters = "!@#$%^&*()-+"    
    with_upper = any([c.isupper() for c in password])
    with_lower = any([c.islower() for c in password])
    with_nums = any([c.isnumeric() for c in password])
    with_special = any([True if c in special_characters else False for c in password])

    missing = 0
    shortLength = 6 - n
    missing += 1 if not with_lower else 0
    missing += 1 if not with_nums else 0
    missing += 1 if not with_upper else 0
    missing += 1 if not with_special else 0
        
    return shortLength if shortLength >= missing else missing

def minimumNumber2(n, password):
    special_characters = "!@#$%^&*()-+"
    no_upper = no_lower = no_nums = no_special = True
    
    for c in password:
        if c.isupper():
            no_upper = False
        if c.islower():
            no_lower = False
        if c.isnumeric():
            no_nums = False
        if c in special_characters:
            no_special = False
    
    missing = 0
    shortLength = 6 - n
    missing += 1 if no_lower else 0
    missing += 1 if no_upper else 0
    missing += 1 if no_nums else 0
    missing += 1 if no_special else 0
        
    return shortLength if shortLength >= missing else missing

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
