class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        res=[]
        idx=0
        while(idx<len(intervals)):
            temp=[0]*2
            temp[0]=intervals[idx][0]
            end=intervals[idx][1]
            while(idx<len(intervals)-1 and intervals[idx+1][0]<=end):
                idx+=1
                end=max(end,intervals[idx][1])
            temp[1]=end
            res.append(temp)
            idx+=1
        return res
