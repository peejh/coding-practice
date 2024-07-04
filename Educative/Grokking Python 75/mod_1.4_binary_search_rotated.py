# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5157082961674240/4539068708945920

def binary_search_rotated(nums, target):
  low, high = 0, len(nums) - 1
  mid = (low + high) // 2

  while high >= low:
    
    # band-aid solution as logic breaks down when there are 2 elements left
    if high - low < 3:
      if nums[low] == target:
        return low
      elif nums[high] == target:
        return high

    if nums[mid] == target:
      return mid
    
    if nums[low] <= nums[mid] and (target < nums[mid] and target >= nums[low]): # first half sorted
      high = mid - 1
    elif nums[low] >= nums[mid] and (target < nums[mid] or target >= nums[low]): # first half not sorted
      high = mid - 1
    else:
      low = mid + 1

    mid = (low + high) // 2

  return -1