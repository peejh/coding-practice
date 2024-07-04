# https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby
S = input()
print(*[(sum(1 for _ in g), int(k)) for k, g in groupby(S)], sep=' ')
# print(*[(len(list(g)), int(k)) for k, g in groupby(S)], sep=' ')