from collections import defaultdict
class Solution(object):
    def findMaxLength(self, nums):
        hm=defaultdict(int)
        k=0
        prefix=0
        hm[0]=-1
        ans=0
        for i in range(len(nums)):
            if(nums[i]==1):
                prefix+=1
            else:
                prefix-=1
            if(prefix-k in hm):
                ans=max(ans,i-hm[prefix-k])
            if(prefix in hm):
                pass
            else:
                hm[prefix]=i
        return ans