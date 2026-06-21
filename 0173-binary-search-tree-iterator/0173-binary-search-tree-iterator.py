# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        self.stack=[]
        temp=root
        while(temp!=None):
            self.stack.append(temp)
            temp=temp.left
        #print(stack)

    def next(self):
        node=self.stack[-1]
        ans=node.val
        self.stack.pop()
        if(node.right!=None):
            temp=node.right
            while(temp!=None):
                self.stack.append(temp)
                temp=temp.left
        return ans
        

    def hasNext(self):
        if(self.stack!=[]):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()