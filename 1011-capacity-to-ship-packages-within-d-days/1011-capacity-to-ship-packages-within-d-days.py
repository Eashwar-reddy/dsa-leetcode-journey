class Solution(object):
    def shipWithinDays(self, weights, days):
        def cal(cap):
            day=0
            load=0
            for i in weights:
                if(load+i>cap):
                    day+=1
                    load=i
                else:
                    load+=i
            if(load>0):
                day+=1
            return day<=days
        low=max(weights)
        high=sum(weights)
        ans=low
        while(low<=high):
            mid=(low+high)//2
            if(cal(mid)):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans