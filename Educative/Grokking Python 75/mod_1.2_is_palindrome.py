# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5157082961674240/5234687148687360

def is_palindrome(s):
  s_len = len(s)
  for i in range(0, s_len // 2):
    if s[i] != s[s_len - 1 - i]:
      return False
  return True

def is_palindrome2(s):
  return s == ''.join(reversed(s))