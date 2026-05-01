class Solution(object):
    def productExceptSelf(self, nums):
        prefix=[0]*len(nums)
        suffix=[0]*(len(nums))
        prefix[0]=suffix[-1]=1
        for i in range(1,len(nums)):
            prefix[i]=nums[i-1]*prefix[i-1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        res=[]
        for i in range(len(nums)):
            res.append(suffix[i]*prefix[i])
        return res