from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        hm=defaultdict(int)
        hm[0]=1
        s=0
        count=0
        for num in nums:
            s+=num
            count+=hm[s-k]
            hm[s]+=1
        return count
            
