# https://www.hackerrank.com/challenges/organizing-containers-of-balls/
# Difficulty: MEDIUM

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from bisect import insort

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    '''
    NOTES:

    The approach taken in this working solution is different from the
    optimal solution because of the following incorrect assumptions
    that were considered:
    - the objective is to sort the balls such that there is only one
      color type in each container
    - a color can exceed the next highest available container capacity
      and its leftover can spill onto another container of smaller
      capacity
      e.g.
            n = 3
            3   
            1 3
            1
      with 3 containers, 5 balls of the first color, and 3 balls of
      the second color can be sorted as follows
            4   <- 4 balls of 1st color into 4 capacity container
            3   <- 3 balls of 2nd color into 3 capacity container
            1   <- 1 ball of 1st color into 1 capacity container

    This approach ignores details about swapping and conceptually
    sorts balls into containers with a specified starting capacity.
    A solution is 'possible' if the balls can be sorted into the
    containers.    
    '''

    n = len(container) # number of containers
    
    # count the capacity of each container
    color_type_count = 0
    container_sizes = []

    for c in container:
        container_sizes.append(sum(c))
        color_type_count = max(color_type_count, len(c))
        
    container_sizes = sorted(container_sizes, reverse=True)

    # find the total number of balls for each color
    ball_counts = [0 for _ in range(color_type_count)]
    
    for r in range(n): # row
        for c in range(len(container[r])): # column
            ball_counts[c] += container[r][c]
    
    ball_counts = sorted(ball_counts, reverse=True)
    
    # match the ball count to the container sizes
    while len(container_sizes) > 0 and len(ball_counts) > 0:
        bc = ball_counts[0]
        cs = container_sizes[0]
        ball_counts = ball_counts[1:]
        container_sizes = container_sizes[1:]

        # consider case when the ball count exceeds the next
        # highest available container capacity
        if bc > cs:
            diff = bc - cs
            ball_counts.append(diff)
            ball_counts = sorted(ball_counts, reverse=True)
    
    # a solution is 'impossible' if there are not enough containers
    # for the balls
    if len(container_sizes) == 0 and len(ball_counts) > 0:
        return 'Impossible'
            
    return 'Possible'

def organizingContainers_best(container):
    '''
    NOTES:
    This solution breaks when the containers are of different length,
    i.e. the counts of each color is not tracked by all containers
    '''
    
    container_sizes = sorted(map(sum, container))
    ball_counts = sorted(map(sum, zip(*container)))
    return "Possible" if container_sizes == ball_counts else "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()