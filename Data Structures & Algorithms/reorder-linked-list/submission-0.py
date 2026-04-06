# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow.next
        slow.next = None
        # reverse latter half
        prev = None
        while middle:
            nextUp = middle.next
            middle.next = prev
            prev = middle
            middle = nextUp
        curr1 = head
        curr2 = prev
        while curr2:
            temp1, temp2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = temp1
            curr1, curr2 = temp1, temp2

# [0,1,2]
# [6,5,4,3]



