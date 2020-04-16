# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        p = l1
        q = l2
        while p != None:
            stack1.append(p.val)
            p = p.next
        while q != None:
            stack2.append(q.val)
            q = q.next
        r = 0
        ans = None
        while stack1 or stack2 or r != 0:
            a = b = 0
            if len(stack1) > 0:
                a = stack1.pop()
            if len(stack2) > 0:
                b = stack2.pop()
            print(a, b)
            s = (a + b + r) % 10
            r = (a + b + r) / 10
            node = ListNode(s)
            node.next = ans
            ans = node
        return ans

s = Solution()
l1 = ListNode(7)
l1.next = ListNode(2)
l2 = ListNode(5)
print(s.addTwoNumbers(l1, l2))