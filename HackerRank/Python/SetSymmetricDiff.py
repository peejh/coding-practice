# https://www.hackerrank.com/challenges/symmetric-difference/problem

M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))

ab_diff = a.difference(b)
ba_diff = b.difference(a)

[print(num) for num in sorted(ab_diff.union(ba_diff))]