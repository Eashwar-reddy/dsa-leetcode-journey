class Solution(object):
    def letterCasePermutation(self, s):
        temp=s[:]
        temp=temp.upper()
        ans=[]
        def generate(s,temp,idx,res):
            if(idx==len(s)):
                ans.append(res[:])
                return 
            if(ord(s[idx])>=48 and ord(s[idx])<=57):
                generate(s,temp,idx+1,res+s[idx])
            else:
                generate(s,temp,idx+1,res+temp[idx].lower())
                generate(s,temp,idx+1,res+temp[idx])
        generate(s,temp,0,"")
        return ans