T = int(input()) # number of test cases

for _ in range(T):
    a_count = int(input())
    A = set(map(int, input().split()))
    b_count = int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B))