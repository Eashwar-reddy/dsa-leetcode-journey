class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if(len(flowerbed)==1):
            if(flowerbed[0]==0):
                n-=1
                flowerbed[0]=1
        for i in range(len(flowerbed)):
            if(n>0):
                if(i==0 and flowerbed[i]==0 and len(flowerbed)>1):
                    if(flowerbed[i+1]==0):
                        n-=1
                        flowerbed[i]=1
                elif(i==len(flowerbed)-1 and flowerbed[i]==0):
                    if(flowerbed[i-1]==0):
                        n-=1
                        flowerbed[i]=1
                else:
                    if(flowerbed[i]==0):
                        if(flowerbed[i-1]==0 and flowerbed[i+1]==0):
                            n-=1
                            flowerbed[i]=1
            else:
                break
        return True if n<=0 else False