class Solution(object):
    def generateParenthesis(self, n):
        res=[]
        def generate(open,close,s):
            if(len(s)==2*n):
                res.append(s)
                return
            if(open<n):
                generate(open+1,close,s+"(")
            if(close<open):
                generate(open,close+1,s+")")
        generate(0,0,"")
        return res