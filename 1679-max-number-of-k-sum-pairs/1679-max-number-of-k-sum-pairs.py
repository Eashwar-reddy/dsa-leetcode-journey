from collections import defaultdict
class Solution(object):
    def maxOperations(self, nums, k):
        hm=defaultdict(int)
        count=0
        for i in nums:
            if(hm[k-i]>0):
                hm[k-i]-=1
                count+=1
            else:
                hm[i]+=1
        return count