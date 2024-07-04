# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re

def sol1():
    S = input()
    pattern = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'
    m = re.findall(pattern, S)
    print(*m, sep='\n') if m else print(-1)

def sol2():
    S = input()
    pattern = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'
    m = re.finditer(pattern, S)
    if m:
        [print(sub.group(1)) for sub in m]
    else:
        print(-1)

def sol3():
    pattern = '(?<=[^aeiou\s\d\W_])([aeiou]{2,})(?=[^aeiou\s\d\W_])'
    lst = re.findall(rf'{pattern}', input(), re.IGNORECASE) # combined r and f strings
    if lst:
        print(*lst, sep='\n')
    else:
        print(-1)