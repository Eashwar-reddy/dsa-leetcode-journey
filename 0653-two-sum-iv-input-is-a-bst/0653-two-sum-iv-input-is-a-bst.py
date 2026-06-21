# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        arr=[]
        def inorder(root):
            if(root!=None):
                inorder(root.left)
                arr.append(root.val)
                inorder(root.right)
        inorder(root)
        p1=0
        p2=len(arr)-1
        while(p1<p2):
            if(arr[p1]+arr[p2]>k):
                p2-=1
            elif(arr[p1]+arr[p2]<k):
                p1+=1
            else:
                return True
        return False