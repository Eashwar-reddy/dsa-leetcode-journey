class Solution(object):
    def longestPalindrome(self, s):
        start=-1
        res=0
        for  i in range(len(s)):
            l=i
            r=i
            count=0
            while(l>=0 and r<len(s) and s[l]==s[r]):
                count=r-l+1
                if(count>res):
                    res=count
                    start=l
                l-=1
                r+=1
            l=i
            r=i+1
            count=0
            while(l>=0 and r<len(s) and s[l]==s[r]):
                count=r-l+1
                if(count>res):
                    res=count
                    start=l
                l-=1
                r+=1
        return s[start:start+res]