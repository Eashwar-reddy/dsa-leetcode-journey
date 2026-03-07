class Solution(object):
    def longestValidParentheses(self, s):
        stack=[-1]
        #count=0
        n=len(s)
        ans=0
        for i in range(n):
            if(s[i]=='('):
                #count+=2
                stack.append(i)
            else:
                stack.pop()
                if(stack==[]):
                    stack.append(i)
                else:
                    ans=max(ans,i-stack[-1])
                    #stack.append(i)
            '''else:
                stack.append(i)'''
        return ans