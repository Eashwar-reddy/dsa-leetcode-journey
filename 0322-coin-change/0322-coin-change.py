class Solution(object):
    def coinChange(self, coins, amount):
        dp=[[-1]*(amount+1) for i in range(len(coins))]
        def fun(ind,t,dp):
            if(ind==0):
                if(t%coins[ind]==0):
                    return t//coins[ind]
                else:
                    return float('inf')
            if(dp[ind][t]!=-1):
                return dp[ind][t]
            nottake=0+fun(ind-1,t,dp)
            take=float('inf')
            if(coins[ind]<=t):
                take=1+fun(ind,t-coins[ind],dp)
            dp[ind][t]=min(take,nottake)
            return dp[ind][t]
        temp=fun(len(coins)-1,amount,dp)
        if(temp==float('inf')):
            return -1
        return temp