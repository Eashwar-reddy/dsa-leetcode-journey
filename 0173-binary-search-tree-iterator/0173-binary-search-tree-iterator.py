# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        self.arr=[]
        temp=root
        def inorder(root):
            if(root!=None):
                inorder(root.left)
                self.arr.append(root.val)
                inorder(root.right)
        inorder(temp)
        self.i=-1
        self.n=len(self.arr)
    def next(self):
        self.i+=1
        if(self.i<self.n):
            return self.arr[self.i]
        else:
            return None

    def hasNext(self):
        if(self.i+1<self.n):
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()