#Longest Common Prefix - Grind75 & TIQ

strs = ["flower","flow","flows"]

#Approach : String & GenProg
#TC : O(mn), SC: O(m)
#m = length of min length string
def func(strs):
    out,i = strs[0],1
    while(i < len(strs)):
        j = 0
        while(j < min(len(out),len(strs[i])) and out[j] == strs[i][j]): j = j+1
        out,i = out[:j],i+1
    return out

print(func(strs))