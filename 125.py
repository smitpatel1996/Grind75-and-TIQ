#Valid Palindrome

s = "A man, a plan, a canal: Panama"

#Approach : String
#TC : O(n), SC: O(1)
def func(s):
    import re
    st = re.sub(r'[^a-z0-9]','', s.lower())
    start,end = 0,len(st)-1
    while(start < end):
        if(st[start] != st[end]): return False
        start,end = start+1,end-1
    return True

print(func(s))