# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        return self.check(root,float("-inf"),float("inf"))
    def check(self,root,li,ui):
        if(root==None):
            return True
        if(root.val<=li or root.val>=ui):
            return False
        return ((self.check(root.left,li,root.val) and self.check(root.right,root.val,ui)))