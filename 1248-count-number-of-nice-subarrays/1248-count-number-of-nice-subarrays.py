from collections import defaultdict
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        def cla(k):
            hm=defaultdict(int)
            l=0
            r=0
            n=len(nums)
            count=0
            while(r<n):
                if(nums[r]%2==0):
                    hm['even']+=1
                else:
                    hm['odd']+=1
                while(hm['odd']>k):
                    if(nums[l]%2==0):
                        hm['even']-=1
                    else:
                        hm['odd']-=1
                    l+=1
                count+=r-l+1
                r+=1
            return count
        return abs(cla(k)-cla(k-1))