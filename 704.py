#Binary Search

nums = [-1,0,3,5,9,12]
target = 2

#Approach : Searching (Binary Search)
#Recursive Binary Search
#TC : O(logn), SC: O(logn)
def func(nums,target):
    if(not len(nums)): return -1
    def helper(s=0,e=len(nums)-1):
        if(s>e): return -1
        m = int((s+e)/2)
        if(nums[m] == target): return m
        elif(nums[m]>target): return helper(s,m-1)
        else: return helper(m+1,e)
    return helper()

#Iterative Binary Search
#TC : O(logn), SC: O(1)
def func(nums,target):
    s,e = 0,len(nums)-1
    while(s<=e):
        m = int((s+e)/2)
        if(nums[m] == target): return m
        elif(nums[m]>target): s,e = s,m-1
        else: s,e = m+1,e
    return -1

print(func(nums,target))