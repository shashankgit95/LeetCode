# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = head = ListNode() 
        if not l1:
            return l2
        if not l2:
            return l1
        
        value = carry = 0
        while l1 or l2 or carry:
            value = carry

            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next

            remainder = value % 10
            carry = value // 10
            curr.next = ListNode(remainder)
            curr = curr.next

        return head.next