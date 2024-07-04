from collections import deque
import sys

T = int(input()) # number of testcases

for _ in range(T):
    n = int(input()) # number of cubes for current testcase
    d = deque(map(int, input().split()))
    stack = [sys.maxsize]
    
    for _ in range(n):
        curr = d.popleft() if d[0] > d[-1] else d.pop()
        if curr <= stack[-1]:
            stack.append(curr)
        else:
            break
    
    print("No" if len(d) > 0 else "Yes")