# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        p = root
        while len(stack) > 0 or p is not None:
            if p is None:
                p = stack.pop()
                p = p.left
            else:
                stack.append(p)
                res.insert(0, p.val)
                p = p.right

        return res

s = Solution()
print(s.postorderTraversal(None))