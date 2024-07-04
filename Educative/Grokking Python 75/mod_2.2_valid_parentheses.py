# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5359382799974400/4636307305398272

def is_valid(s):

    stack = []

    for c in s:
        if c in "{[(":
            stack.append(c)
        else:
            if not stack: # if c is a closing bracket and the stack is empty
                return False
            top = stack[-1]
            if c == '}' and top == "{":
                stack.pop()
            elif c == ']' and top == '[':
                stack.pop()
            elif c == ')' and top == '(':
                stack.pop()
            else:
                # mismatch found
                return False

    return len(stack) == 0