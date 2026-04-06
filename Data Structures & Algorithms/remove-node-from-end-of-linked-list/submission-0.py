# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #    d 1 2 3 4 5 6 7 8
        #      6  
        #    s.f        
        #  make fast "n" faster
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        for i in range(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next