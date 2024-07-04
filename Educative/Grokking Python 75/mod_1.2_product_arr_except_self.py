# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5157082961674240/4968565371437056

def product_except_self(arr):
    n = len(arr)
    res = [1] * n
    l_prod = 1
    r_prod = 1
    
    for i in range(1, n):
        l_prod *= arr[i-1]
        res[i] *= l_prod

    for i in range(n-2, -1, -1):
        r_prod *= arr[i+1]
        res[i] *= r_prod

    return res

def product_except_self2(arr):
    n = len(arr)
    res = [1] * n
    l_prod = 1
    r_prod = 1
    
    for i in range(1, n):
        l_prod *= arr[i-1]
        res[i] *= l_prod
        r_prod *= arr[-i]
        res[-i-1] *= r_prod

    return res