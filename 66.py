#Plus One

digits = [1,2,3]

#Approach : Arrays
#TC : O(n), SC: O(1)
def func(digits):
    def rev(l):
        s,e = 0,len(l)-1
        while(s<e): 
            l[s],l[e] = l[e],l[s]
            s,e = s+1,e-1
        return l
    t,c = rev(digits),1
    for i in range(len(t)):
        t[i],c = (t[i]+c)%10,int((t[i]+c)/10)
        if(c==0): break
    if(c): t.append(c)
    return rev(t)

print(func(digits))