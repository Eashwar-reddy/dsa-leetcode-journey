# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def height(node):
            if(node==None):
                return 0
            lh=height(node.left)
            rh=height(node.right)
            return 1+max(lh,rh)
        def check(node):
            if(node==None):
                return True
            lh=height(node.left)
            rh=height(node.right)
            if(abs(lh-rh)>1):
                return False
            left=check(node.left)
            right=check(node.right)
            if(not left or not right):
                return False
            return True
        return check(root)
        