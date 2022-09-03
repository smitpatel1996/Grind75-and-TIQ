#Linked List Cycle

#Approach : Linked List
#TC : O(n), SC: O(1)
def func(head):
    if(not head): return False
    s,f = head,head.next
    while(f):
        if(s == f): return True
        elif(not f.next): return False
        s,f = s.next,f.next.next
    return False