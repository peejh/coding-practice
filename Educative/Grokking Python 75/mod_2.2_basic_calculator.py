# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5359382799974400/5417082044940288

def calculator(s):

    # STEP 1: tokenize the input string
    toks = []
    num = ''
    for ch in s:
        if ch.isdigit():
            num += ch
        elif ch == ' ':
            continue
        else:
            if num:
                toks.append(int(num))
                num = ''
            toks.append(ch)
    if num:
        toks.append(int(num))

    # STEP 2: evaluate the arithmetic expression
    ops = "+-"
    symbols = []    # tracks and evaluates non-integer tokens
    lefts = []      # tracks left-hand operands

    for tok in toks:
        if isinstance(tok, int):
            # if a number comes after a plus or minus symbol
            # then perform the operation and store the result
            if symbols and symbols[-1] in ops:
                op = symbols.pop()
                left = lefts.pop()
                if op == '+':
                    left += tok
                else:
                    left -= tok
                lefts.append(left)
            # otherwise store the number
            else:
                lefts.append(tok)
        else:
            if tok in ops:
                # store the operation until we have the right hand operand
                symbols.append(tok)
            elif tok == '(':
                # store the left bracket to prevent out-of-order arithmetic evaluation
                # and preserve evaluation priority for parenthesized expressions
                symbols.append(tok)
            elif tok == ')':
                symbols.pop() # pop the stored opening bracket
                # if there's a pending left-hand operand
                if symbols and symbols[-1] != '(':
                    op = symbols.pop()
                    right = lefts.pop()
                    left = lefts.pop()
                    if op == '+':
                        left += right
                    else:
                        left -= right
                    lefts.append(left)

    return lefts.pop()