# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5157082961674240/4950189555187712

def add_binary(str1, str2):

    result = ""
    m = len(str1)
    n = len(str2)
    max_len = max(m, n)
    str1 = str1.zfill(max_len)
    str2 = str2.zfill(max_len)
    carry = 0
    for i in range(max_len-1, -1, -1):
        curr = carry;
        curr += 1 if str1[i] == '1' else 0
        curr += 1 if str2[i] == '1' else 0
        carry = 1 if curr > 1 else 0
        result += str(curr % 2)
        # print(carry, result)

    result += str(carry) if carry == 1 else ''

    return result[::-1]