from collections import defaultdict
class Solution(object):
    def findCircleNum(self, isConnected):
        n=len(isConnected)
        graph=defaultdict(list)
        for i in range(n):
            for j in range(n):
                if(isConnected[i][j]==1):
                    graph[i].append(j)
        visited=[False]*n
        count=0
        stack=[]
        for i in range(n):
            if(not visited[i]):
                stack.append(i)
                visited[i]=True
                while(stack!=[]):
                    node=stack.pop()
                    for nei in graph[node]:
                        if(not visited[nei]):
                            visited[nei]=True
                            stack.append(nei)
                count+=1
        return count