class Solution(object):
    def strStr(self, haystack, needle):
        i=0
        while(i<len(haystack)-len(needle)+1):
            idx=0
            if(haystack[i]==needle[idx]):
                while(idx<len(needle) and i< len(haystack) and haystack[i+idx]==needle[idx]):
                    idx+=1
            if(idx==len(needle)):
                return i
            i+=1
        return -1