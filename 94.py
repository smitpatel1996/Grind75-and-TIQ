#Binary Tree Inorder Traversal

#Approach : Binary Tree
#Recursive Implementation
#TC : O(n), SC: O(n)
def func(root):
    if(not root): return []
    l = []
    def helper(root):
        if(not root): return
        helper(root.left)
        l.append(root.val)
        helper(root.right)
    helper(root)
    return l

#Iterative Implementation
#TC : O(n), SC: O(n)
def func(root):
    if(not root): return []
    l,s = [],[]
    while(1):
        if(root): 
            s.append(root)
            root = root.left
        elif(len(s)):
            t = s.pop()
            l.append(t.val)
            root = t.right
        else: break
    return l