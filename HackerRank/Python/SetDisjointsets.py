# https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

plus = sum([i in A for i in arr])
minus = sum([i in B for i in arr])
print(plus - minus)