class Solution(object):
    def smallestDivisor(self, nums, threshold):
        def cal(div):
            ans=0
            for i in nums:
                if(i%div==0):
                    ans+=i//div
                else:
                    ans+=(i//div)+1
            if(ans<=threshold):
                return True
            return False
        low=1
        high=max(nums)
        ans=high
        while(low<=high):
            mid=(low+high)//2
            if(cal(mid)):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans