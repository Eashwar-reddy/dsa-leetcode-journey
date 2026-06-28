class Solution(object):
    def maximumPrimeDifference(self, nums):
        primes=[True]*101
        primes[0]=primes[1]=False
        for i in range(2,11):
            if(primes[i]):
                for j in range(i*i,101,i):
                    primes[j]=False
        l=[]
        for i in range(len(nums)):
            if(primes[nums[i]]):
                l.append(i)
        return(max(l)-min(l))