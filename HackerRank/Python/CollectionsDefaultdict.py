# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

def sol1():
    n, m = map(int, input().split())
    insertIdx = defaultdict(list)

    for i in range(1, n+1):
        insertIdx[input()].append(str(i))
    
    for _ in range(m):
        print(*insertIdx[input()] or [-1])

def sol2():
    n, m = map(int, input().split())
    A = defaultdict(list)
    [A[input()].append(str(i)) for i in range(1, n + 1)]
    B = [input() for _ in range(m)]
    print(*[" ".join(A[i]) or "-1" for i in B], sep="\n")

if __name__ == "__main__":
    sol1()
    sol2()