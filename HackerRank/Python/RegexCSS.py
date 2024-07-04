# https://www.hackerrank.com/challenges/hex-color-code/problem

import re

if __name__ == "__main__":
    N = int(input())
    res = []
    
    for _ in range(N):
        line = input()
        pattern = r'[:\s,](#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3})\b'
        # pattern = r'(?<=:.*)(#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3})\b' # with positive lookbehind
        matches = re.findall(pattern, line)
        res.extend(matches)
    
    for color in res:
        print(color)