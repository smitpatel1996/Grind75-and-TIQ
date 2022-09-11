#Invert Binary Tree

#Approach : Binary Trees
#TC : O(n), SC: O(n)
def func(root):
    if(root):
        def helper(root):
            if(not root): return
            if(root.left): helper(root.left)
            if(root.right): helper(root.right)
            root.left,root.right = root.right,root.left
        helper(root)
    return root