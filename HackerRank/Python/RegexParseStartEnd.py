# https://www.hackerrank.com/challenges/re-start-re-end/problem

import re

S = input()
k = input()
out = set()

for i, ch in enumerate(S):
    m = re.search(rf'{k}', S[i:])
    if m:
        out.add((m.start()+i, m.end()+i-1))
    
if len(out) > 0:
    print(*sorted(list(out)), sep='\n')
else:
    print((-1, -1))
# one line if-else
# print(*sorted(list(out)), sep='\n') if len(out) > 0 else print((-1, -1))
