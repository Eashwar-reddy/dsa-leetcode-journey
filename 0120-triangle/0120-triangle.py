class Solution(object):
    def minimumTotal(self, triangle):
        n=len(triangle)
        dp=[]
        for i in range(n):
            dp.append([0]*(i+1))
        dp[0][0]=triangle[0][0]
        for i in range(1,n):
            dp[i][0]=dp[i-1][0]+triangle[i][0]
        for i in range(1,n):
            for j in range(1,i+1):
                if(j==i):
                    dp[i][j]=dp[i-1][j-1]+triangle[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j-1]+triangle[i][j],dp[i-1][j]+triangle[i][j])
        return(min(dp[n-1][:]))