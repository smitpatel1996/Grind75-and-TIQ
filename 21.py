#Merge Two Sorted Lists

#Approach : Linked List
#TC : O(m+n), SC: O(1)
#m,n = len(list1),len(list2)
def func(list1, list2):
    if(not (list1 and list2)): return None
    elif(list1 and not list2): return list1
    elif(not list1 and list2): return list2
    else:
        if(list1.val <= list2.val): head,list1 = list1,list1.next
        else: head,list2 = list2,list2.next
        out = head
        while(list1 and list2):
            if(list1.val <= list2.val): head.next,list1 = list1,list1.next
            else: head.next,list2 = list2,list2.next
            head = head.next
        if(list1): head.next = list1
        else: head.next = list2
    return out