# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5157082961674240/4733237637283840

import re

def myAtoi(s):
    # Trim and take the first word
    result = s.lstrip().split(' ')[0]

    # Check for parseable number in the beginning of the string
    matches = re.match(r'^((-|\+)?\d+)', result)

    # if a match is found
    if matches is not None:
        first = matches.group(1)
        sign = 1
        if first[0] == '-':
            first = first[1:]
            sign = -1
        return sign * int(first)
    
    # if no match
    return 0