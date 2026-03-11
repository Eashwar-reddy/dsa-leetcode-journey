from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        hm=defaultdict(int)
        l=0
        r=0
        n=len(s)
        max_len=0
        max_freq=0
        while(r<n):
            hm[s[r]]+=1
            max_freq=max(max_freq,hm[s[r]])
            if(r-l+1-max_freq>k):
                max_freq=0
                hm[s[l]]-=1
                if(hm[s[l]]==0):
                    del hm[s[l]]
                for i in hm:
                    max_freq=max(max_freq,hm[i])
                l+=1
            if(r-l+1-max_freq<=k):
                max_len=max(max_len,r-l+1)
            r+=1
        return max_len