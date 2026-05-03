# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if(root==None):
            return []
        q=deque()
        q.append(root)
        res=[]
        while(q):
            n=len(q)
            level=[]
            for i in range(n):
                node=q.popleft()
                level.append(node.val)
                if(node.left!=None):
                    q.append(node.left)
                if(node.right!=None):
                    q.append(node.right)
            res.append(level)
        return res   
