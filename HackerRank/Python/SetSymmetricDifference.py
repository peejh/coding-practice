# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

en = int(input())
en_subs = set(map(int, input().split()))
fr = int(input())
fr_subs = set(map(int, input().split()))

print(len(en_subs.symmetric_difference(fr_subs)))
# print(len(en_subs ^ fr_subs))