#Valid Anagram

s = "rat"
t = "car"

#Approach : Hashing
#TC : O(n), SC: O(n)
def func(s,t):
    d = {}
    for i in s:
        if(i in d): d[i] = d[i]+1
        else: d[i] = 1
    for i in t:
        if(i in d): 
            d[i] = d[i]-1
            if(d[i] == 0): d.pop(i)
        else: return False
    if(d): return False
    return True

print(func(s,t))