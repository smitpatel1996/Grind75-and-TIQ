#Merge Sorted Array

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

#Approach : GenProg
#TC : O(m+n), SC: O(1)
def func(nums1,m,nums2,n):
    i,m,n = len(nums1)-1,m-1,n-1
    while(m>=0 and n>=0):
        if(nums2[n] >= nums1[m]): nums1[i],n = nums2[n],n-1
        else: nums1[i],m = nums1[m],m-1
        i = i-1
    if(m<0): 
        while(n>=0): nums1[i],n,i = nums2[n],n-1,i-1
    print(nums1)

func(nums1,m,nums2,n)