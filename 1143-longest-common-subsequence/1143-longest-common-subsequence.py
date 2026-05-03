class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        n=len(text1)
        m=len(text2)
        dp=[[-1]*m for i in range(n)]
        def generate(i,j):
            if(i<0 or j<0):
                return 0
            if(dp[i][j]!=-1):
                return dp[i][j]
            match=-1
            notmatch=-1
            if(text1[i]==text2[j]):
                match=1+generate(i-1,j-1)
            else:
                notmatch=max(generate(i-1,j),generate(i,j-1))
            dp[i][j]= max(match,notmatch)
            return dp[i][j]
        temp=generate(n-1,m-1)
        if(temp==-1):
            return 0
        return temp