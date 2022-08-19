#Roman to Integer - Grind75 & TIQ

s = "MCMXCIV"

#Approach : Math
#TC : O(n), SC: O(1)
def func(s):
    l = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    c,prev,i = l[s[0]],l[s[0]],1
    while(i < len(s)):
        if(l[s[i]] <= prev): c = c+l[s[i]]
        else: c = c+l[s[i]]-2*prev
        prev,i = l[s[i]],i+1
    return c

print(func(s))