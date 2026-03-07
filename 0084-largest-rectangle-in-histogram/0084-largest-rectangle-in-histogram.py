class Solution(object):
    def largestRectangleArea(self, heights):
        n=len(heights)
        nse=[0]*n
        pse=[0]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while(stack!=[] and heights[stack[-1]]>=heights[i]):
                stack.pop()
            if(stack==[]):
                nse[i]=n
            else:
                nse[i]=stack[-1]
            stack.append(i)
        stack=[]
        for i in range(n):
            while(stack!=[] and heights[stack[-1]]>=heights[i]):
                stack.pop()
            if(stack==[]):
                pse[i]=-1
            else:
                pse[i]=stack[-1]
            stack.append(i)
        ans=float('-inf')
        for i in range(n):
            width=(i-pse[i]+nse[i]-i-1)
            area=width*(heights[i])
            ans=max(ans,area)
        return ans
