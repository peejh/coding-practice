# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

pattern = r'^[789]\d{9}$'
for _ in range(int(input())):
    print('YES') if bool(re.match(pattern, input())) else print('NO')