class Solution(object):
    def change(self, amount, coins):
        n=len(coins)
        dp=[[-1]*(amount+1) for i in range(n)]
        def fun(ind,t):
            if(ind==0):
                if(t%coins[ind]==0):
                    return 1
                else:
                    return 0
            if(dp[ind][t]!=-1):
                return dp[ind][t]
            nottake=fun(ind-1,t)
            take=0
            if(coins[ind]<=t):
                take=fun(ind,t-coins[ind])
            dp[ind][t]= take+nottake
            return dp[ind][t]
        return fun(n-1,amount)