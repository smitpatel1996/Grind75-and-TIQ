#Two Sum - Grind75 & TIQ

nums = [3,3]
target = 6

#Approach : Hashing
#TC : O(n), SC: O(n)
def func(nums, target):
    d,i = {},0
    while(i < len(nums)):
        if(nums[i] in d): return [d[nums[i]],i]
        d[target-nums[i]] = i
        i=i+1

print(func(nums,target))