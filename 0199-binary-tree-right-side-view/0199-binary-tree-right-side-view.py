# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution(object):
    def rightSideView(self, root):
        res=[]
        def fun(node,l):
            #global res
            if(node==None):
                return
            #hm[l].append(node.val)
            #fun(node.left,l+1)
            if(l==len(res)):
                res.append(node.val)
            fun(node.right,l+1)
            fun(node.left,l+1)
        fun(root,0)
        return res
