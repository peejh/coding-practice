# https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict

counts = OrderedDict()

for _ in range(int(input())):
    word = input()
    counts[word] = 1 + (counts[word] if word in counts else 0)

print(len(counts))
print(*counts.values())