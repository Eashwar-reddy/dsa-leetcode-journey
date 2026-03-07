class Solution(object):
    def maxArea(self,arr,n):
        pse=[0]*n
        nse=[0]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while(stack!=[] and arr[stack[-1]]>=arr[i]):
                stack.pop()
            if(stack==[]):
                nse[i]=n
            else:
                nse[i]=stack[-1]
            stack.append(i)
        stack=[]
        for i in range(n):
            while(stack!=[] and arr[stack[-1]]>=arr[i]):
                stack.pop()
            if(stack==[]):
                pse[i]=-1
            else:
                pse[i]=stack[-1]
            stack.append(i)
        ans=float('-inf')
        for i in range(n):
            width=(i-pse[i]+nse[i]-i-1)
            area=arr[i]*width
            ans=max(ans,area)
        return ans
    def maximalRectangle(self, matrix):
        m=len(matrix[0])
        n=len(matrix)
        ans=float('-inf')
        for i in range(m):
            count=0
            for j in range(n):
                count+=1
                if(matrix[j][i]=='0'):
                    count=0
                matrix[j][i]=count
        for i in matrix:
            ans=max(ans,self.maxArea(i,m))
        return ans