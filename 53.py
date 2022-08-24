#Maximum Subarray

nums = [-2,1,-3,4,-1,2,1,-5,4]

#Approach : DP
#TC : O(n), SC: O(1)
#Kadane's Algorithm
def func(nums):
    cm,gm,i = nums[0],nums[0],1
    while(i<len(nums)):
        cm = max(nums[i],cm+nums[i])
        gm = max(cm,gm)
        i=i+1
    return gm

print(func(nums))

#Try Divide and Conquer Approach too.
#TC : O(nlogn), SC: O(1)