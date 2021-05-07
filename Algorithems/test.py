class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse(head):
    cur = head
    p = None
    while cur:
        q = cur.next
        cur.next = p
        p = cur
        cur = q
    return p

def merge(node1, node2):
    dummy = Node(0)
    p = dummy
    p1, p2 = node1, node2
    while p1 and p2:
        if p1.val < p2.val:
            p = p.next = p1
            p1 = p1.next
        else:
            p = p.next = p2
            p2 = p2.next
    while p1:
        p = p.next = p1
        p1 = p1.next
    while p2:
        p = p.next = p2
        p2 = p2.next
    return dummy.next
    


def func(head):
    odd_head = head
    even_head = head.next
    p2 = even_head
    p = p1 = odd_head
    count = 1
    while p:
        if count % 2 == 0:
            p2 = p2.next = p
        else:
            p1 = p1.next = p
        p = p.next
        count += 1

    even_head = reverse(even_head)
    merge(odd_head, even_head)