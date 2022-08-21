#Implement strStr()

haystack = "aaaaa"
needle = "bba"

#Approach : String
#TC : O(n*m), SC: O(1)
#n=len(haystack), m=len(needle)
def func(haystack,needle):
    s,e = 0,len(needle)
    while(e<=len(haystack)):
        if(haystack[s:e] == needle): return s
        s,e = s+1,e+1
    return -1

print(func(haystack,needle))