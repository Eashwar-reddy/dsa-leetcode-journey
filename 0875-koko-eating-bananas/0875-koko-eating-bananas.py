class Solution(object):
    def minEatingSpeed(self, piles, h):
        def calculate(k):
            ans=0
            for i in piles:
                if(i%k==0):
                    ans+=(i//k)
                else:
                    ans+=(i//k)+1
            if(ans<=h):
                return ans
            return -1
        low=1
        high=max(piles)
        res=high
        while(low<=high):
            mid=(low+high)//2
            temp=calculate(mid)
            if(temp==-1):
                low=mid+1
            else:
                res=min(mid,res)
                high=mid-1
        return res