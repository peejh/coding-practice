# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5157082961674240/6315161468141568

def binary_search(nums, target):

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        
        if target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1