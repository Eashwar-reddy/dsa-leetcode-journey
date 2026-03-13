from collections import defaultdict
class Solution(object):
    def checkSubarraySum(self, nums, k):
        n=len(nums)
        prefix=0
        hm=defaultdict(int)
        hm[0]=-1
        for i in range(0,n):
            prefix+=nums[i]
            temp=prefix%k
            if(temp in hm):
                if(i-hm[temp]>1):
                    return True
            else:
                hm[temp]=i
        return False