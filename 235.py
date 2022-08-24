#Lowest Common Ancestor of a Binary Search Tree

#Approach : BST
#TC : O(logn), SC: O(logn)
def func(root,p,q):
    if(not root): return None
    pv,qv = min(p.val,q.val),max(p.val,q.val)
    def helper(root):
        if(root.val > qv): return helper(root.left)
        if(root.val < pv): return helper(root.right)
        return root
    return helper(root)