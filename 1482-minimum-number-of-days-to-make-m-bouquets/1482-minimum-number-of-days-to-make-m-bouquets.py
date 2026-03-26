class Solution(object):
    def minDays(self, bloomDay, m, k):
        def bloom(day):
            count=0
            bouq=0
            for i in bloomDay:
                if(i<=day):
                    count+=1
                else:
                    bouq+=(count//k)
                    count=0
            bouq+=(count//k)
            if(bouq>=m):
                return True
            return False
        if(len(bloomDay)<(m*k)):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        ans=high
        while(low<=high):
            mid=(low+high)//2
            if(bloom(mid)):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
