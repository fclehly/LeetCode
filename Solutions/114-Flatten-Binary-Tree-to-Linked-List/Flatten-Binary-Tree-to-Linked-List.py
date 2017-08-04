# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        ans = TreeNode(-1)
        p = ans
        def postOrder(node):
            if node is not None:
                p.right = TreeNode(node.x)
                p = p.right
                postOrder(node.left)
                postOrder(node.right)
        return ans.right
solutin = Solution()

        
