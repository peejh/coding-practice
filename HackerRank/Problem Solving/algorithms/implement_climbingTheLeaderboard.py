# https://www.hackerrank.com/challenges/climbing-the-leaderboard
# Difficulty: MEDIUM

#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect, insort

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    '''
    To find each of the player score its position in the `ranked` list,
    we return the index the score will have if it is inserted into the
    `ranked` list while maintaining its descending order    
    '''

    # Insert 1e10, or any number higher than the constraints of this problem, at
    # index 0 and duplicate scores are removed. This is so a score's given index
    # corresponds to its rank.
    # Each score is turned negative because the `bisect` method does not work
    # with a descending list.
    ranked = [n * -1 for n in sorted(set([1e10] + ranked), reverse=True)]
    ans = []

    for score in player:
        score *= -1
        # `bisect` returns the index where `score` can be inserted to `ranked`
        # while maintaning the order of the list
        # `bisect` executes with a time complexity of O(log n)
        idx = bisect(ranked, score)

        if ranked[idx-1] == score: # Check if `score` already exists
            # If so, return that index
            ans.append(idx-1)
        else:
            # Otherwise, return the index provided by `bisect`
            ans.append(idx)

            # The following are ways to insert a value in an ordered list with
            # decent runtimes
            # However, these are not really required as the scores in the
            # `player` list are in ascending order, which means earlier inserts
            # do not affect the position of later inserts
            # Hence, actual inserts can be skipped to save on runtime
            # insort(ranked, score, idx) # O(log n)
            # ranked = ranked[:idx] + [score] + ranked[idx:] # O(n)

    return ans
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
