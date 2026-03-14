from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res=0
        seen=set()
        l=0
        r=0
        while(r<len(s)):
            if(s[r] in seen):
                while(s[r] in seen):
                   seen.discard(s[l])
                   l+=1
            seen.add(s[r])
            res=max(res,len(seen))
            r+=1
        return res

        