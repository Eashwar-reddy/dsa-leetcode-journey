class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        grid=obstacleGrid[:]
        n=len(grid)
        m=len(grid[0])
        dp=[[0]*m for i in range(n)]
        if(grid[0][0]==1):
            return 0
        else:
            dp[0][0]=1
        for i in range(1,m):
            if(grid[0][i]==1):
                break
            dp[0][i]=1
        for i in range(1,n):
            if(grid[i][0]==1):
                break
            dp[i][0]=1
        for i in range(1,n):
            for j in range(1,m):
                if(grid[i][j]==1):
                    continue
                dp[i][j]=(dp[i-1][j] if (dp[i-1][j]!=0) else 0)+(dp[i][j-1] if(dp[i][j-1]!=0) else 0)
        return dp[n-1][m-1] 
        