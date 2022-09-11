#Add Binary

a = "1010"
b = "1011"

#Approach: GenProg
#TC : O(n+m), SC: O(1)
#n,m = len(a),len(b)
def func(a,b):
    def doSum(n,c):
        t = n+c
        if(t>1): return str(t%2),1 
        else: return str(t),0
    ai,bi,c,s = len(a)-1,len(b)-1,0,[]
    while(ai>=0 and bi>=0):
        t,c = doSum(int(a[ai])+int(b[bi]),c)
        s.append(t)
        ai,bi=ai-1,bi-1
        print(s)
    while(ai>=0):
        t,c = doSum(int(a[ai]),c)
        s.append(t)
        ai=ai-1
    while(bi>=0):
        t,c = doSum(int(b[bi]),c)
        s.append(t)
        bi=bi-1
    if(c): s.append("1")
    return "".join(s[::-1])

print(func(a,b))