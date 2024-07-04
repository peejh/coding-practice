# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(string, max_width):
    # res = str()
    # counter = max_width
    # for ch in string:
    #     if counter > 0:
    #         res += ch
    #         counter -= 1
    #     else:
    #         res += f"\n{ch}"
    #         counter = max_width - 1
    # return res
    toks = textwrap.wrap(string, max_width)
    res = str()
    for tok in toks:
        res += tok + '\n'
    return res

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)