#Single Number

nums = [4,1,2,1,2]

#Approach: GenProg
#TC : O(n), SC: O(1)
def func(nums):
    c = nums[0]
    for i in range(1,len(nums)): c = c^nums[i]
    return c

print(func(nums))