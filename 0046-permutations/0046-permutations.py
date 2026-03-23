class Solution(object):
    def permute(self, nums):
        n=len(nums)
        visited=[False]*n
        def rec(temp,visited,count):
            if(count==len(nums)):
                l.append(temp[:])
                return
            for i in range(n):
                if(not visited[i]):
                    visited[i]=True
                    temp.append(nums[i])
                    rec(temp,visited,count+1)
                    temp.pop()
                    visited[i]=False
        l=[]
        temp=[]
        rec(temp,visited,0)
        return l