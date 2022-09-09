#Maximum Depth of Binary Tree

#Approach : Binary Trees and Queues
#TC: O(n), SC: O(2^h)
#h = max-height of the binary tree (2^h < n)
from collections import deque
def func(root):
    if(not root): return 0
    q,d = deque([(root,1)]),1
    while(len(q)):
        t = q.popleft()
        if(t[0].left): 
            q.append((t[0].left,t[1]+1))
            if(t[1]+1>d): d=t[1]+1
        if(t[0].right): 
            q.append((t[0].right,t[1]+1))
            if(t[1]+1>d): d=t[1]+1
    return d