class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            temp=i
            idx=0
            if(haystack[i]==needle[idx]):
                while(idx<len(needle) and temp< len(haystack) and haystack[temp]==needle[idx]):
                    idx+=1
                    temp+=1
            if(idx==len(needle)):
                return i
        return -1