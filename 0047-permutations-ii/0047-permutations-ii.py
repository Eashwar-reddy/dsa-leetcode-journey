from collections import defaultdict
class Solution(object):
    def permuteUnique(self, nums):
        n=len(nums)
        visited=[False]*n
        l=defaultdict(int)
        temp=[]
        def generate(temp):
            if(len(temp)==len(nums)):
                l[tuple(temp[:])]+=1
                return
            for i in range(n):
                if(not visited[i]):
                    temp.append(nums[i])
                    visited[i]=True
                    generate(temp)
                    temp.pop()
                    visited[i]=False
        for i in range(n):
            visited[i]=True
            temp.append(nums[i])
            generate(temp)
            temp.pop()
            visited[i]=False
        return list(l.keys())
        