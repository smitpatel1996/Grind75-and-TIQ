#Climbing Stairs

n = 10

#Approach : DP
#TC : O(n), SC: O(n)
def func(n):
    d = {0:1,1:1}
    def helper(n):
        if(n not in d): d[n] = helper(n-1)+helper(n-2)
        return d[n]
    return helper(n)

print(func(n))