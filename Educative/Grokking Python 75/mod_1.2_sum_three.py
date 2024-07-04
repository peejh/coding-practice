# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/5157082961674240/6452609548419072

def find_sum_of_three(nums, target):
   if len(nums) < 3:
      return False
   
   nums.sort()
   
   for i in range(len(nums)):
      j = i + 1
      k = len(nums) - 1
      while j < k:
         sum = nums[i] + nums[j] + nums[k]
         if sum > target:
            k -= 1
         elif sum < target:
            j += 1
         else:
            return True

   return False

if __name__ == "__main__":   
   print(find_sum_of_three([1,-1,0], -1)) # false
   print(find_sum_of_three([3,7,1,2,8,4,5], 10)) # true
   print(find_sum_of_three([3,7,1,2,8,4,5], 21)) # false
   print(find_sum_of_three([-1,2,1,-4,5,-3], -8)) # true
   print(find_sum_of_three([-1,2,1,-4,5,-3], 0)) # true