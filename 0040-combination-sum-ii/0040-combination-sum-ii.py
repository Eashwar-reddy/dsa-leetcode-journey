#from collections import defaultdict
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        def subset(candidates,idx,sum,temp):
            if(sum==target):
                l.append(temp[:])
            if(sum>target):
                return
            for i in range(idx,len(candidates)):
                if(i>idx and candidates[i]==candidates[i-1]):
                    continue
                temp.append(candidates[i])
                subset(candidates,i+1,sum+candidates[i],temp)
                temp.pop()
        l=[]
        temp=[]
        subset(candidates,0,0,temp)
        return l