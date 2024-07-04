# https://www.hackerrank.com/challenges/py-set-add/problem

N = int(input())
countries = set()
[countries.add(input()) for _ in range(N)]
print(len(countries))