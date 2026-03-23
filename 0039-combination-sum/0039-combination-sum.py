class Solution(object):
    def combinationSum(self, candidates, target):
        nums=candidates[:]
        def sub(idx,sum,temp):
            if(sum==target):
                l.append(temp[:])
                return
            if(sum>target):
                return
            if(idx==len(nums)):
                return
            sub(idx+1,sum,temp)
            temp.append(nums[idx])
            sub(idx,sum+nums[idx],temp)
            temp.pop()
        l=[]
        temp=[]
        sub(0,0,temp)
        return l