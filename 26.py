#Remove Duplicates from Sorted Array

nums = [0,0,1,1,1,2,2,3,3,4]

#Approach : Array
#TC : O(n), SC: O(n)
def func1(nums):
    i,l,m = 1,[nums[0]],0
    while(i<len(nums)):
        if(nums[i] != nums[m]):
            l.append(nums[i])
            m,i = i,i+1
        i=i+1
    return len(l),l
print(func1(nums))

#Approach : Array
#TC : O(n), SC: O(1)
#Inplace : Non-Duplicates pushed to front.
def func2(nums):
    fast,slow,c,m = 1,1,1,0
    while(fast<len(nums)):
        if(nums[fast] != nums[m]): nums[slow],m,c,slow = nums[fast],fast,c+1,slow+1
        fast = fast+1
    return c
print(func2(nums))