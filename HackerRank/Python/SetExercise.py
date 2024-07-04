# https://www.hackerrank.com/challenges/py-check-subset/problem

if __name__ == "__main__":
    T = int(input()) # number of test cases
    for _ in range(T):
        countA = int(input())
        A = set(map(int, input().split()))
        countB = int(input())
        B = set(map(int, input().split()))
        print(A.issubset(B))