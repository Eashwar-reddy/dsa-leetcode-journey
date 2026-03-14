from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        length=0
        pos=defaultdict(int)
        start=0
        for end in range(len(s)):
            ch=s[end]
            if(pos[ch]>0 and pos[ch]-1>= start):
                start=pos[ch]       
            pos[ch]=end+1 
            length=max(length,end-start+1)
        return length

        