class Solution(object):
    def splitArray(self, nums, k):
        def split(val,k):
            temp=0
            count=1
            for i in nums:
                if(temp+i>val):
                    count+=1
                    temp=i
                else:
                    temp+=i
            return count
        low=max(nums)
        high=sum(nums)
        res=float('inf')
        while(low<=high):
            mid=(low+high)//2
            count=split(mid,k)
            if(count<=k):
                res=min(res,mid)
                high=mid-1
            else:
                low=mid+1
        return res 