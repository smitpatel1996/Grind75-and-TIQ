#Convert Sorted Array to Binary Search Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

nums = [-10,-3,0,5,9]

#Approach: Binary Search Tree
#TC : O(n), SC: O(logn)
def func(nums):
    def helper(s=0,e=len(nums)-1):
        if(s>e): return None
        m = int((s+e)/2)
        t = TreeNode(nums[m])
        t.left,t.right = helper(s,m-1),helper(m+1,e)
        return t
    return helper()