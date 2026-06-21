class Solution(object):
    def kthSmallest(self, root, k):
        count = [0]
        def inorder(root):
            #nonlocal count
            if not root:
                return None
            left = inorder(root.left)
            if left is not None:
                return left
            count[0] += 1
            if count[0] == k:
                return root.val
            return inorder(root.right)
        return inorder(root)
