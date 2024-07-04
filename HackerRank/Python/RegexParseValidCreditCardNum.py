# https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import re

# pattern = re.compile(r'(?!.*(\d)(-?\1{3}|\1-?\1{2}|\1{2}-?\1).*)^[456]\d{3}(-?\d{4}){3}$')
pattern = re.compile(r'^(?=.*(\d)(-?\1){3}.*)[456]\d{3}(-?\d{4}){3}$')
for _ in range(int(input())):
    line = input().strip()
    if bool(re.match(pattern, line)):
        print("Valid")
    else:
        print("Invalid")