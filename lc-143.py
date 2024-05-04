# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        while(fast.next != None) and (fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        second_curr = slow.next
        slow.next = None

        second_curr = self.reverseList(second_curr)
        curr = head


        while second_curr != None:
            temp1, temp2 = curr.next, second_curr.next
            curr.next = second_curr
            second_curr.next = temp1
            curr, second_curr = temp1,temp2

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
