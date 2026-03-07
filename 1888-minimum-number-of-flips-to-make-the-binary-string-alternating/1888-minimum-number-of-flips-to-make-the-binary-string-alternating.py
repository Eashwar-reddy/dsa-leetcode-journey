class Solution(object):
    def minFlips(self, s):
        n=len(s)
        s=s+s
        s1=""
        s2=""
        temp=True
        for i in range(2*n):
            if(temp):
                s1+='0'
                s2+='1'
            else:
                s1+='1'
                s2+='0'
            temp=not temp
        dif1=0
        dif2=0
        nn=2*n
        ans=float('inf')
        for i in range(n):
            if(s[i]!=s1[i]):
                dif1+=1
            if(s[i]!=s2[i]):
                dif2+=1
            '''else:
                pass'''
        ans=min(ans,dif1,dif2)
        for i in range(n,nn):
            if(s[i-n]!=s1[i-n]):
                dif1-=1
            if(s[i-n]!=s2[i-n]):
                dif2-=1
            '''else:
                pass'''
            if(s[i]!=s1[i]):
                dif1+=1
            else:
                dif2+=1
            ans=min(ans,dif1,dif2)
        return ans
            
        