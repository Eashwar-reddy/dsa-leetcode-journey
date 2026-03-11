class Solution(object):
    def bitwiseComplement(self, n):
        s=bin(n)[2:]
        s=s.replace('1','-1')
        s=s.replace('0','1')
        s=s.replace('-1','0')
        return int(s,2)