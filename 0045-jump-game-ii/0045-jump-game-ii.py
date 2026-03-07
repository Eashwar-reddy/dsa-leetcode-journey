class Solution(object):
    def jump(self, nums):
        n=len(nums)
        l=0
        r=0
        jumps=0
        while(r<n-1):
            far=0
            for j in range(l,r+1):
                far=max(far,j+nums[j])
            l=r+1
            r=far
            jumps+=1
        return jumps