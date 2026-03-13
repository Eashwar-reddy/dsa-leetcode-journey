class Solution(object):
    def isPalindrome(self, s):
        seen='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        seen=set(list(seen))
        n=len(s)
        l=0
        r=n-1
        while(l<=r):
            if(s[l] in seen and s[r] in seen):
                t1=s[l:l+1].lower()
                t2=s[r:r+1].lower()
                if(t1==t2):
                    l+=1
                    r-=1
                else:
                    return False
            else:
                if(s[l] not in seen):
                    l+=1
                    
                else:
                    r-=1
                    continue
        return True