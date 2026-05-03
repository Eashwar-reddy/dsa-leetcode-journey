# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        path1=[]
        path2=[]
        def getPath(node,path,target):
            if(node==None):
                return False
            path.append(node)
            if(node==target):
                return True
            if(getPath(node.left,path,target) or getPath(node.right,path,target)):
                return True
            path.pop()
            return False
        getPath(root,path1,p)
        getPath(root,path2,q)
        i=0
        n=len(path1)
        m=len(path2)
        while(i<min(n,m) and path1[i]==path2[i]):
            i+=1
        return path1[i-1]
