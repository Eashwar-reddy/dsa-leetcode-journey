from collections import defaultdict
class Solution(object):
    def totalFruit(self, fruits):
        hm=defaultdict(int)
        l=0
        r=0
        n=len(fruits)
        max_len=0
        res=0
        while(r<n):
            hm[fruits[r]]+=1
            max_len+=1
            while(len(hm)>2):
                hm[fruits[l]]-=1
                max_len-=1
                if(hm[fruits[l]]==0):
                    del hm[fruits[l]]
                l+=1
            if(len(hm)<=2):
                res=max(max_len,res)
            r+=1
        return res