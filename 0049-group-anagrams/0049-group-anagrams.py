from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        hm=defaultdict(list)
        for i in strs:
            temp="".join(sorted(i))
            hm[temp].append(i)
        res=[]
        for i in hm:
            res.append(hm[i])
        return res