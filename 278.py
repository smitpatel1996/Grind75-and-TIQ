#First Bad Version

#Approach : Binary Search
#Iterative Implementation
#TC : O(logn), SC: O(1)
def func(n):
    s,e = 1,n
    while(s<=e):
        m=int((s+e)/2)
        if(isBadVersion(m)): s,e = s,m-1
        else: s,e = m+1,e
    return s