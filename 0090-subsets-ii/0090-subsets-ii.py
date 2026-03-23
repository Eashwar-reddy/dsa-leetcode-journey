class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        def subset(idx,nums,temp):
            l.append(temp[:])
            for i in range(idx,len(nums)):
                if(i>idx and nums[i]==nums[i-1]):
                    continue
                temp.append(nums[i])
                subset(i+1,nums,temp)
                temp.pop()
        l=[]
        temp=[]
        subset(0,nums,temp)
        return l