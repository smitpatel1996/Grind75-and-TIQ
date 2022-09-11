#Majority Element

nums = [2,2,1,1,1,2,2]

#Approach: Greedy
#TC : O(n), SC: O(1)
def func(nums):
    m,c,i = nums[0],1,1
    while(i<len(nums)):
        if(nums[i]==m): c=c+1
        else: c=c-1
        if(c<0): m,c = nums[i],1
        i=i+1
    return m

print(func(nums))