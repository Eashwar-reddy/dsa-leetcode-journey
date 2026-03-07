class Solution(object):
    def trap(self, height):
        n=len(height)
        prefix=[0]*n
        suffix=[0]*n
        prefix[0]=height[0]
        for i in range(1,n):
            prefix[i]=max(prefix[i-1],height[i])
        suffix[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            suffix[i]=max(suffix[i+1],height[i])
        total=0
        for i in range(n):
            if(height[i]<prefix[i] and height[i]<suffix[i]):
                total+=min(prefix[i],suffix[i])-height[i]
        return total
