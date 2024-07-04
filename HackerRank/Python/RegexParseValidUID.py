# https://www.hackerrank.com/challenges/validating-uid/problem

import re

UID = r'^(?!.*(.).*\1)(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)[^\W_]{10}$'

T = int(input())
for _ in range(T):
    if bool(re.match(UID, input())):
        print("Valid")
    else:
        print("Invalid")
    # print("Valid") if bool(re.match(UID, input())) else print("Invalid")