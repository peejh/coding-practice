# https://www.hackerrank.com/challenges/acm-icpc-team
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    max_topic = 0 # max number of topics known by any 2-person team
    max_teams = 0 # number of teams that know the max number of topics
    # Count the number of topics for each possible 2-person team
    for comb in combinations(topic, 2):
        # Convert the binary strings into integers so they can
        # be mathematically operated on
        a, b = map(lambda x: int(x, 2), comb)
        # Perform a bitwise OR between the 2 persons of a team,
        # convert it to a binary string, and count the 1s
        topic_count = bin(a | b).count('1')
        # Adjust `max_topic` and `max_teams` accordingly
        if topic_count > max_topic:
            max_topic = topic_count
            max_teams = 0
        if topic_count == max_topic:
            max_teams += 1
    
    return [max_topic, max_teams]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()