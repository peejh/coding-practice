# https://www.hackerrank.com/challenges/smart-number
# Difficulty: EASY

import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    if val * val == num: # CHANGE; perfect squares have odd factors
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")