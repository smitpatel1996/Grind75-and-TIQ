#Intersection of Two Linked Lists

#Approach: Linked List
#TC : O(n+m), SC: O(1)
#n,m = len(llA),len(llB)
def func(headA, headB):
    tA,tB,c = headA,headB,0
    while(headA and headB): headA,headB = headA.next,headB.next
    if(not headA):
        while(headB): headB,c = headB.next,c+1
        while(c): tB,c = tB.next,c-1
    if(not headB):
        while(headA): headA,c = headA.next,c+1
        while(c): tA,c = tA.next,c-1
    while(tA!=tB): tA,tB = tA.next,tB.next
    return tA