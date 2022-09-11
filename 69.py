#Sqrt(x)

x = 80

#Approach : Binary Search
#TC : O(logn), SC: O(1)
def func(x):
    if(x in (0,1)): return x
    s,e = 1,int(x/2)
    while(s<=e):
        m = int((s+e)/2)
        if(m*m == x): return m
        elif(m*m > x): s,e = s,m-1
        else: s,e = m+1,e
    return e

print(func(x))