class Solution(object):
    def numIslands(self, grid):
        n=len(grid)
        m=len(grid[0])
        visited=[[False]*m for i in range(n)]
        def dfs(i,j):
            if(i>=n or j>=m or i<0 or j<0):
                return 
            if(grid[i][j]=='0' or visited[i][j]):
                return
            visited[i][j]=True
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        count=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]=='1' and (not visited[i][j])):
                    dfs(i,j)
                    count+=1
        return count
