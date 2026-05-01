class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total=nums[0]
        currmin=globalmin=nums[0]
        currmax=globalmax=nums[0]
        for i in nums[1:]:
            currmin=min(currmin+i,i)
            globalmin=min(globalmin,currmin)
            currmax=max(currmax+i,i)
            globalmax=max(currmax,globalmax)
            total+=i
        if(globalmax<0):
            return globalmax
        return max(globalmax,total-globalmin)