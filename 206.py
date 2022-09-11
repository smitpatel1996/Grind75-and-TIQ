#Reverse Linked List

#Approach: Linked List
#TC : O(n), SC: O(1)
def func(head):
    if(not head): return head
    p,c,n = None,head,head.next
    while(n): c.next,p,c,n = p,c,n,n.next
    c.next = p
    return c