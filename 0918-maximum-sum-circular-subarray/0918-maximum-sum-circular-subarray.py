class Solution(object):
    def maxSubarraySumCircular(self, nums):
        currmax=globalmax=nums[0]
        currmin=globalmin=nums[0]
        total=nums[0]
        for i in nums[1:]:
            currmax=max(currmax+i,i)
            globalmax=max(globalmax,currmax)
            currmin=min(currmin+i,i)
            globalmin=min(currmin,globalmin)
            total+=i
        if(globalmax<0):
            return globalmax
        return(max(globalmax,total-globalmin))
