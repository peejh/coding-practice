# https://www.hackerrank.com/challenges/py-set-union/problem

en = int(input())
en_subs = set(map(int, input().split()))
fr = int(input())
fr_subs = set(map(int, input().split()))

print(len(en_subs.union(fr_subs)))
# print(len(en_subs | fr_subs))