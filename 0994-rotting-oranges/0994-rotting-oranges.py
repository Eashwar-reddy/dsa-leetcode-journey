from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        n=len(grid)
        m=len(grid[0])
        visited=[[0]*m for i in range(n)]
        q=deque()
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==2):
                    visited[i][j]=2
                    q.append((i,j,0))
        drow=[0,-1,1,0]
        dcol=[-1,0,0,1]
        tm=0
        while(q):
            r,c,tm=q.popleft()
            for i in range(4):
                nr=r+drow[i]
                nc=c+dcol[i]
                #if()
                if(nr<n and nc<m and nr>=0 and nc>=0 and visited[nr][nc]!=2 and grid[nr][nc]==1):
                    visited[nr][nc]=2
                    q.append((nr,nc,tm+1))
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1 and visited[i][j]!=2):
                    return -1
        return tm
