#Flood Fill

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

#Approach : Recursion & 2D Arrays
#TC : O(n), SC: O(n) (recursive call stack)
def func(image,sr,sc,color):
    if(image[sr][sc] != color):
        t = image[sr][sc]
        def helper(r=sr,c=sc):
            image[r][c] = color
            if(r-1>=0 and image[r-1][c]==t): helper(r-1,c)
            if(r+1<len(image) and image[r+1][c]==t): helper(r+1,c)
            if(c-1>=0 and image[r][c-1]==t): helper(r,c-1)
            if(c+1<len(image[0]) and image[r][c+1]==t): helper(r,c+1)
        helper()
    return image

print(func(image,sr,sc,color))