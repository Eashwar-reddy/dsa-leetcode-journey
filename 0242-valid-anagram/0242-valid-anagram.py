from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        hm=defaultdict(int)
        for i in s:
            hm[i]+=1
        for i in t:
            hm[i]-=1
        for i in hm:
            if(hm[i]!=0):
                return False
        return True