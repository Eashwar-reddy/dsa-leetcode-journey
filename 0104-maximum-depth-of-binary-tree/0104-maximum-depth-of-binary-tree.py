# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        def fun(node):
            if(node==None):
                return 0
            left=fun(node.left)
            right=fun(node.right)
            return 1+max(left,right)
        return fun(root)