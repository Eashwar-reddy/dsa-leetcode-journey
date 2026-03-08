from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n=len(nums)
        ans=[]
        dq=deque()
        for i in range(k):
            while(dq and nums[dq[-1]]<nums[i]):
                dq.pop()
            dq.append(i)
        ans.append(nums[dq[0]])
        for i in range(k,n):
            if(dq[0]<i-k+1):
                dq.popleft()
            while(dq and nums[dq[-1]]<nums[i]):
                dq.pop()
            dq.append(i)
            ans.append(nums[dq[0]])
        return ans
            