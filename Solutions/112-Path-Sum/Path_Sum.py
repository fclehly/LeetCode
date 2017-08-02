# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs(node, res):
            if node is not None:
                r = res - node.val
                if r == 0:
                    return True
                elif r > 0:
                    return dfs(node.left, r) or dfs(node.right, r)
                else:
                    return False
            return False
        return dfs(root, sum)