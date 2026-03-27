class Solution(object):
    def findKthPositive(self, arr, k):
        if(len(arr)==1):
            if(arr[0]==1):
                return 2
            if(arr[0]<k):
                return k+k-arr[0]
            return arr[0]-1
        miss_arr=[]
        for i in range(len(arr)):
            miss_arr.append(arr[i]-i-1)
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            if(miss_arr[mid]<k):
                low=mid+1
            else:
                high=mid-1
        
        return(low+k)