# https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re

T = int(input())
pattern = re.compile(r'^[\+\-]?\d*\.[\d]{1,}$')
for _ in range(T):
    s = input().strip()
    print(pattern.match(s) is not None)
    # if pattern.match(s) is not None:
    #     try:
    #         n = float(s)
    #         print(True)
    #     except ValueError:
    #         print(False)
    # else:
    #     print(False)