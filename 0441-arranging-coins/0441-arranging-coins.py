class Solution(object):
    def arrangeCoins(self, n):
        ans=0
        count=0
        while(ans<=n):
            if(ans+1<=n):
                ans=ans+1
                n=n-ans
                count+=1 
            else:
                ans=n+1
        return count