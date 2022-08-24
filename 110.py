#Balanced Binary Tree

def func(root):
    if(not root): return True
    def helper(root):
        if(not root): return (True,-1)
        l,r = helper(root.left),helper(root.right)
        print(root.val,l,r)
        if(l[0] and r[0] and abs(l[1]-r[1])<=1): return (True,max(l[1],r[1])+1)
        else: return (False,max(l[1],r[1])+1)
    return helper(root)[0]