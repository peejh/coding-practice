def check_palindrome(txt):
    if len(txt) == 1:
        return True
    low = 0
    high = len(txt) - 1
    while low < high:
        if txt[low] != txt[high]:
            return False
        low += 1
        high -= 1
    return True

def sol():
    N, arr = int(input()), input().split()
    is_all_positive = all([int(i) > 0 for i in arr])
    is_any_palindromic = any([check_palindrome(i) for i in arr])
    # another popular alternative to above line, but has O(n log n) runtime
    # is_any_palindromic = any([i == ''.join(reversed(i)) for i in arr])
    print(is_all_positive and is_any_palindromic)