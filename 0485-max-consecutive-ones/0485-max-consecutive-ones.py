class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        i=0
        res=0
        n=len(nums)
        while(i<n and nums[i]!=1):
            i+=1
        for j in range(i,n):
            if(nums[j]==1):
                count+=1
            else:
                res=max(res,count)
                count=0
        res=max(res,count)
        return res