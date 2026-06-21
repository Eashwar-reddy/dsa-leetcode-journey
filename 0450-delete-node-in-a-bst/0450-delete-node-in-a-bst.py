# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        if(root==None):
            return None
        if(root.val>key):
            root.left=self.deleteNode(root.left,key)
        elif(root.val<key):
            root.right=self.deleteNode(root.right,key)
        else:
            if(root.left==None):
                return root.right
            if(root.right==None):
                return root.left
            lastRight=self.findLastRight(root.left)
            lastRight.right=root.right
            return root.left
        return root
    def findLastRight(self,root):
        while(root.right!=None):
            root=root.right
        return root