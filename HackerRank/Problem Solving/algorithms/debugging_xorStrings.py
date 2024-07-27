# https://www.hackerrank.com/challenges/strings-xor
# Difficulty: EASY

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]: # CHANGE 1
            res += '0' # CHANGE 2
        else:
            res += '1' # CHANGE 3

    return res

s = input()
t = input()
print(strings_xor(s, t))