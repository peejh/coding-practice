# https://www.hackerrank.com/challenges/py-set-mutations/problem

a_len = int(input())
A = set(map(int, input().split()))
for _ in range(int(input())):
    op = input().split()[0]
    other = set(map(int, input().split()))
    eval(f"A.{op}(other)")
print(sum(A))