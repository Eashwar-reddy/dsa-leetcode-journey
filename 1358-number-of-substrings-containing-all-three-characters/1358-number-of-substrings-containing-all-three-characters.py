from collections import defaultdict
class Solution(object):
    def numberOfSubstrings(self, s):
        n=len(s)
        l=0
        r=0
        hm=defaultdict(int)
        ans=0
        while(r<n):
            hm[s[r]]+=1
            while(len(hm)==3):
                ans+=(n-r)
                hm[s[l]]-=1
                if(hm[s[l]]==0):
                    del hm[s[l]]
                l+=1
            r+=1
        return ans
