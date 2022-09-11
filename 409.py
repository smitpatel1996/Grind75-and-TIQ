#Longest Palindrome

s = "adam"

#Approach: Hashing
#TC : O(n+m), SC: O(m)
#n,m = len(s),len(set(s))
def func(s):
    d,c,odd = {},0,False
    for i in s:
        if(i in d): d[i] = d[i]+1
        else: d[i] = 1
    for i in d:
        if(d[i]%2 == 0): c = c+d[i]
        else: c,odd = c+d[i]-1,True
    if(odd): c=c+1
    return c

print(func(s))