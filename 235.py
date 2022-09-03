#Lowest Common Ancestor of a Binary Search Tree

#Approach : BST
#TC : O(logn), SC: O(logn)
def func(root,p,q):
    if(not root): return root
    pv,qv = min(p.val,q.val),max(p.val,q.val)
    def helper(root):
        if(root.val > qv): return helper(root.left)
        if(root.val < pv): return helper(root.right)
        return root
    return helper(root)

#Iterative Implementation
#TC : O(logn), SC: O(1)
def func(root,p,q):
    if(not root): return root
    pv,qv = min(p.val,q.val),max(p.val,q.val)
    while(root):
        if(root.val > qv): root = root.left
        elif(root.val < pv): root = root.right
        else: break
    return root


#Lowest Common Ancestor of a Binary Tree

#Approach : Binary Trees
#TC : O(n), SC: O(n)
def func(root,p,q):
    if(not root): return root
    def helper(root):
        if(not root): return root
        if(root.val in (p.val,q.val)): return root
        l,r = helper(root.left),helper(root.right)
        if(l and r): return root
        else:
            if(l): return helper(root.left)
            else: return helper(root.right)
    return helper(root)