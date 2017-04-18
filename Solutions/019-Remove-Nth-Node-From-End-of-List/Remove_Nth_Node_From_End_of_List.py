# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        vir_head = ListNode(0)
        vir_head.next = head
        p, q = vir_head, vir_head

        for i in range(n):
            p = p.next

        while p.next:
            p = p.next
            q = q.next

        t = q.next
        q.next = t.next
        del t
        return vir_head.next

    def printList(self, head):
        if head is not None:
            p = head
            while p is not None:
                print(p.val)
                p = p.next
s = Solution()
a = ListNode(0)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
e = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = e
s.removeNthFromEnd(a, 5)
s.printList(a)