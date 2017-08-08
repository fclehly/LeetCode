# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        node1, node2 = ListNode(-1), ListNode(-1)
        p, q = node1, node2
        while head is not None:
            if head.val < x:
                p.next = head
                p = p.next
            else:
                q.next = head
                q = q.next
            head = head.next
        q.next = None
        p.next = node2.next
        return node1.next

def createListNode(vals):
    if vals is None or len(vals) == 0:
        return None
    head = ListNode(-1)
    tail = head
    for i, val in enumerate(vals):
        tail.next = ListNode(val)
        tail = tail.next
    return head.next

def printListNode(head):
    if head is None:
        print(None)
    else:
        p = head
        while p is not None:
            print(p.val)
            p = p.next

s = Solution()
head = createListNode([1, 4, 3, 2, 5, 2])
printListNode(head)
print("-----")
printListNode(s.partition(head, 3))
print('-----------')