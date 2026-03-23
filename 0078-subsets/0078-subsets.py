class Solution(object):
    def subsets(self, nums):
        def subset(idx,nums,temp):
            if(idx==len(nums)):
                l.append(temp[:])
                return
            subset(idx+1,nums,temp)
            temp.append(nums[idx])
            subset(idx+1,nums,temp)
            temp.pop()
        l=[]
        temp=[]
        subset(0,nums,temp)
        return l