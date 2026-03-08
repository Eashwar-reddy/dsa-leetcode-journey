class Solution(object):
    def findDifferentBinaryString(self, nums):
        n=len(nums)
        seen=set()
        for i in range(n):
            nums[i]=int(nums[i],2)
        nums=set(nums)
        for i in range(n+1):
            if(i not in nums):
                ans=format(i,'0{}b'.format(n))
                return ans