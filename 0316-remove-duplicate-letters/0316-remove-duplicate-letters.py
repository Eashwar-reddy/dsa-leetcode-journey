from collections import defaultdict
class Solution(object):
    def removeDuplicateLetters(self, s):
        hm=defaultdict(int)
        for c in s:
            hm[c]+=1
        stack=[]
        seen=set()
        for c in s:
            hm[c]-=1
            if c in seen:
                continue
            while(stack and stack[-1]>c and hm[stack[-1]]>0):
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        return "".join(stack)