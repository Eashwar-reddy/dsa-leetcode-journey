class Solution(object):
    def maxDistance(self, position, m):
        position.sort()
        def cal(dis,m):
            point=position[0]
            m-=1
            for i in range(1,len(position)):
                if(position[i]-point>=dis):
                    m-=1
                    point=position[i]
            return m<=0
        low=1
        high=max(position)-min(position)
        ans=low
        while(low<=high):
            mid=(low+high)//2
            if(cal(mid,m)):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans