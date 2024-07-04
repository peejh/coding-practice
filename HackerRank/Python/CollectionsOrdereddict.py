# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

grocery = OrderedDict()

for _ in range(int(input())):
    *name, price = input().split()
    name = ' '.join(name)
    if name in grocery:
        grocery[name] += int(price)
    else:
        grocery[name] = int(price)
    
for k, v in grocery.items():
    print(k, v)