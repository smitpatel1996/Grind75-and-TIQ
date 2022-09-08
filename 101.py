#Symmetric Tree

#Approach : Binary Trees
#Recursive Implementation
#TC : O(n), SC: O(n)
def func(root):
    if(not root): return True
    def helper(n1, n2):
        if(n1==None and n2==None): return True
        elif((n1==None and n2!=None) or (n1!=None and n2==None)): return False 
        else:
            if(n1.val!=n2.val): return False
            else: return (helper(n1.left,n2.right) and helper(n1.right,n2.left))
    return helper(root.left,root.right)