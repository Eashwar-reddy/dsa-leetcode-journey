class Solution(object):
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0])
        row=0
        col=m-1
        while(row<n and col>=0):
            if(matrix[row][col]==target):
                return 1
            elif(matrix[row][col]>target):
                col-=1
            else:
                row+=1
        return 0