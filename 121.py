#Best Time to Buy and Sell Stock

prices = [7,6,4,3,1]

#Approach : DP (but simpler)
#TC : O(n), SC: O(1)
#Extra Feature : Returns Days of Buy and Sell too.
def func(prices):
    b,i,mp,days = 0,1,0,None
    while(i < len(prices)):
        if(prices[i]<=prices[b]): b=i
        else:
            t = prices[i]-prices[b]
            if(t > mp): mp,days = t,(b,i)
        i=i+1
    return mp
    #return mp,days

print(func(prices))