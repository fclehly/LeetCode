# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # return False
        def isValid(node, min, max):
            if node is None:
                return True
            if node.val <= min or node.val >= max:
                return False
            else:
                return isValid(node.left, min, root.val) and isValid(node.right, root.val, max)
        return isValid(root, -2 ** 63, 2 ** 63 - 1)
    

def list2tree(l):
    if l == None and len(l) < 1:
        return False
    root = TreeNode(l[0])
    for 

s = Solution()
root = TreeNode(1)
root.left = TreeNode(1)
# root.right = TreeNode(3)
# print(2 ** 31 - 1)
print(s.isValidBST(root))

        