#Ransom Note

ransomNote = "aa"
magazine = "aab"

#Approach: Hashing
#TC : O(n+m), SC: O(k)
#n,m,k = len(ransomNote),len(magazine),len(set(magazine))
def func(ransomNote, magazine):
    d = {}
    for i in magazine:
        if(i in d): d[i] = d[i]+1
        else: d[i] = 1
    for i in ransomNote:
        if(i not in d): return False
        else:
            d[i] = d[i]-1
            if(d[i] == 0): del d[i]
    return True

print(func(ransomNote, magazine))