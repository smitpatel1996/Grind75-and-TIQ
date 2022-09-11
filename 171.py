#Excel Sheet Column Number

columnTitle = "AAA"

#Approach: GenProg
#TC : O(n), SC: O(1)
def func(columnTitle):
    c,p = 0,0
    for i in reversed(columnTitle): c,p = c+((26**p)*(ord(i)-ord("A")+1)),p+1
    return c

print(func(columnTitle))