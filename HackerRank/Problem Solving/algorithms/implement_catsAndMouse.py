# https://www.hackerrank.com/challenges/cats-and-a-mouse

#!/bin/python3

import math
import os
import random
import re
import sys

def catAndMouse(x, y, z):
    '''
    > to minimize confusion, this solution assumes that x <= z <= y
    '''
    
    left, right = 'Cat A', 'Cat B'
    
    # switch variables around when x > y
    if x > y:
        x, y = y, x
        left, right = right, left
    
    distA = z - x
    distB = y - z
    
    if x == y or distA == distB:
        return 'Mouse C'
    elif x > z or distA < distB:
        return left
    
    return right
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
