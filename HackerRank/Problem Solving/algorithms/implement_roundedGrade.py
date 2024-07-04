# https://www.hackerrank.com/challenges/grading

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    result = []
    for g in grades:
        if g < 38:
            result.append(g)
            continue
        nextceilfive = nextCeilFive(g)
        print(g, nextceilfive)
        result.append(nextceilfive if nextceilfive - g < 3 else g)
    return result

def nextCeilFive(n):
    ceils = [num for num in range(100, 39, -5)]
    result = 100
    
    for c in ceils:
        if c < n:
            break
        result = c

    return result

def gradingStudents_v2(grades):
    result = []
    for g in grades:
        rounded = (g + 5) - (g % 5) if g > 37 and g % 5 > 2 else g
        # rounded = ((g // 5) + 1) * 5 if g > 37 and g % 5 > 2 else g # alternative
        result.append(rounded)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
