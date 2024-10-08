# https://www.hackerrank.com/challenges/yet-another-minimax-problem

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations, combinations

#
# Complete the 'anotherMinimaxProblem' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def anotherMinimaxProblem(a):
    '''
    > this solution comes from the observation that a max score from a 
    permutation of `a` occurs when a number with a higher significant bit
    is XORed with a number that has a lower significant bit.
    > the final answer is then derived from finding the minimum among the
    max scores.
    '''

    # screen for input with only 0s
    if all(x == 0 for x in a):
        return 0

    # find the most significant bit of the highest number in `a`
    n = len(a)
    max_bit = max(a).bit_length()

    # partition the elements of `a`
    # comparisons start at the highest possible msb
    for bit in range(max_bit - 1, -1, -1):
        msb = 1 << bit # most significant bit
        with_msb, without_msb = [], []

        # partition numbers into groups that has the current msb
        # on vs those that don't
        for num in a:
            if num & msb:
                with_msb.append(num)
            else:
                without_msb.append(num)

        # break out of the loop when we have clear partitions
        if with_msb and without_msb:
            break
    
    # when no clear partitions can be made, return the minimum among
    # all possible scores
    if not without_msb or not with_msb:
        return min(a[i] ^ a[j] for i in range(n) for j in range(i + 1, n))

    # when there are clear partitions, return the minimum among the possible
    # scores from XORing numbers between the two groups
    return min(x ^ y for x in without_msb for y in with_msb)    

def anotherMinimaxProblem_wrongtry(a):
    '''
    based on a wrong assumption
    if we have a sorted list of all possible scores,
    the minimum max is the nth-1 highest possible score
    where n is the number of items in a
    '''
    scores = set()
    for x, y in combinations(a, 2):
        # print(x, y)
        scores.add(x ^ y)
    scores = sorted(list(scores))
    idx = len(a) - 1
    idx = -idx if len(scores) >= idx else 0
    print(scores)
    return scores[idx]

def anotherMinimaxProblem_bruteForce(a):
    scores = []
    for perm in permutations(a):
        scores.append(max([perm[i] ^ perm[i-1] for i in range(1, len(perm))]))
    return min(scores)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = anotherMinimaxProblem(a)

    fptr.write(str(result) + '\n')

    fptr.close()

    # SAMPLE TESTCASE
    # numbers = '62353 6196 68326 102493 65195 103531 106480 27959 119007 42299 28050 71147 117860 85342 114790 88952 12582 119398 119104 67434 85208 46253 61575 15655 24966 88054 67531 46113 89337 72175 42300 68958 57906 72567 15363 116958 42766 120168 62982 117476 83286 9778 27906 102989 98651 27191 83025 119879 9625 85198 122181 30525 61327 89599 101581 82661 46749 121942 99451 99944 84091 70494 104669 69184 84348 45631 102243 59178 12059 119776 62615 121941 119646 86347 64779 27656 99686 41880 9268 67174 87003 44844 117607 73081 28049 29756 115790 42038 73043 12933 117970 68707 105184 41378 28416 71913 88548 59530 47494 70343 67690 27780 26550 31136 16270 84420 115789 89203 85583 106187 69104 99183 119544 63890 99451 41631 89287 66022 64564 15418 69625 57788 86471 42543 105838 8726 10257 26375 82424 44457 122363 8983 48696 45569 106177 73714 14513 121726 66130 47896 48668 15278 58537 83404 44033 31923 65993 60592 29478 89174 103920 30521 85972 103284 117066 71791 88030 31271 13106 82687 103412 57405 64904 13112 48657 9241 11038 63031 119523 10666 86138 11428 82769 48942 103910 13616 116089 43688 9403 46983 42659 82163 117078 62757 122110 13875 10135 121564 73087 83540 16283 63287 42172 14096 27797 100421 46652 15759 120405 26006 10015 57638 27779 115952 105935 29973 46370 30746 57358 16182 13607 42146 28571 101499 71700 48663 9734 66909 65028 116957 47142 70503 120150 15893 87371 42162 67418 13975 57731 68455 10664 118908 31410 115963 88307 67833 40989 42396 67550 44094 28705 99062 119158 12701 65990 46618 29727 62253 11315 44854 85347 61116 104167 64675 121679 70134 104808 67799 15124 42672 69082 48779 104171 65052 28444 41748 59191 68471 41860 71107 82646 116474 14618 11914 70397 89209 62217 10513 85752 103898 15145 58758 13481 13441 32392 62864 13961 88177 121946 85571 85629 67068 117487 67552 83524 65893 11685 121810 70082 59911'
    # a = list(map(int, numbers.split()))
    # print(anotherMinimaxProblem(a))
