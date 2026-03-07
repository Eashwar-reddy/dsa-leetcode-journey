class Solution(object):
    def removeKdigits(self, num, k):
        stack=[]
        for i in num:
            while(stack!=[] and int(stack[-1])>int(i) and k!=0):
                stack.pop()
                k-=1
            stack.append(i)
        while(k!=0):
            stack.pop()
            k-=1
        count=0
        for i in stack:
            if(i=='0'):
                count+=1
            else:
                break
        stack=stack[count::]
        ans="".join(stack)
        if(ans==""):
            return '0'
        return ans