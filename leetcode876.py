from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = head
        m = head
        while c is not None:
            if c.next is None:
                return m
            if c.next is not None:
                c = c.next
                m = m.next
            if c.next is not None:
                c = c.next
            else:
                return m
        return m