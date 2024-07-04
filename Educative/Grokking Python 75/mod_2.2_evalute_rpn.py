# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5359382799974400/5148320557301760

import re
import math

def rpn(tokens):
    
    stack = []

    for tok in tokens:
        validnum = r'-?\d+' # official solution doesn't use this
                            # to avoid regex, just switch around the if/else
        if re.match(validnum, tok):
            stack.append(int(tok))
        else:
            right = stack.pop()
            left = stack.pop()
            result = 0
            if tok == '+':
                result = left + right
            elif tok == '-':
                result = left - right
            elif tok == '*':
                result = left * right
            elif tok == '/':
                result = left / right
                result = math.ceil(result) if result < 0 else math.floor(result) # use math.trunc() instead
            stack.append(result)
    
    return stack.pop()