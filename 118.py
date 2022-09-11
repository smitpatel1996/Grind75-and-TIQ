#Pascal's Triangle

numRows = 5

#Approach: GenProg
#TC : O(n^2), SC: O(n^2)
def func(numRows):
    if(numRows == 1): return [[1]]
    elif(numRows == 2): return [[1],[1,1]]
    else:
        l,s = [[1],[1,1]],3
        while(s<=numRows):
            t = [1]
            for i in range(len(l[s-2])-1): t.append(l[s-2][i]+l[s-2][i+1])
            t.append(1)
            l.append(t)
            s = s+1
        return l

print(func(numRows))