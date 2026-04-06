# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # keep track of carry: add to new nodes
        # keep adding till both lists & carry run out
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            val_sum = val1 + val2 + carry
            carry = 1 if val_sum > 9 else 0
            val_sum = val_sum % 10
        
            curr.next = ListNode(val_sum)
            curr = curr.next
        return dummy.next