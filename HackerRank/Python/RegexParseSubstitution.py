import re

def replace(match):
    toks = {'&&': 'and', '||': 'or'}
    return toks[match.group(1)]

def sol1():
    N = int(input())
    src = ""
    for _ in range(N):
        line = input()
        src += line + '\n'
    src = re.sub(r'(?<= )&&(?= )', 'and', src)
    src = re.sub(r'(?<= )\|\|(?= )', 'or', src)
    print(src)

def sol2():
    N = int(input())
    src = "".join([input() + '\n' for _ in range(N)])
    src = re.sub(r'(?<= )(&&|\|\|)(?= )', replace, src)
    print(src.strip())