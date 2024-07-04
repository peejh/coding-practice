# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque

def sol1():
    d = deque()
    switch = {
        'append': lambda x: d.append(x[1]),
        'appendleft': lambda x: d.appendleft(x[1]),
        'pop': lambda x: d.pop(),
        'popleft': lambda x: d.popleft()
    }

    for _ in range(int(input())):
        op = input().split()
        switch[op[0]](op)

    print(*d)

# uses `eval` function
def sol2():
    N = int(input())
    d = deque()
    for _ in range(N):
        method = input().split()
        if len(method) == 1:
            eval(f"d.{method[0]}()")
        else:
            eval(f"d.{method[0]}({method[1]})")
    print(*d)