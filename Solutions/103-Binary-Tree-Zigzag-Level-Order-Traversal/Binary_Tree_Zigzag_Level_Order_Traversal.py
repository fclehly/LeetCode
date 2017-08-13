# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [[root, 0]]
        res = []
        while len(queue) > 0:
            cur = queue.pop()
            node, level = cur[0], cur[1]
            if node.left is not None:
                queue.insert(0, [node.left, level + 1])
            if node.right is not None:
                queue.insert(0, [node.right, level + 1])
            if level > len(res) - 1:
                res.append([])
            if level % 2 == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)
        return res

s = Solution()
a = []
for i in range(0, 10):
    a.append(TreeNode(i))
root = a[0]
root.left = a[1]
root.right = a[2]
a[1].left = a[5]
a[2].left = a[3]
a[2].right = a[4]
# print(root.right.left.val)

print(s.zigzagLevelOrder(root))