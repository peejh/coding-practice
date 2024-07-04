# https://www.hackerrank.com/challenges/day-of-the-programmer

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    when_leap = "12.09."
    when_not_leap = "13.09."
    when_1918 = "26.09.1918"
    ans = ""
    
    if year == 1918:
        ans = when_1918
    elif year < 1918 and year % 4 == 0:
        ans = when_leap + str(year)
    elif year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        ans = when_leap + str(year)
    else:
        ans = when_not_leap + str(year)
    
    return ans
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
