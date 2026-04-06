# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        node = head
        while node:
            node = node.next
            count += 1
        if count < k:
            return head
        
        total_groups = count // k

        dummy = ListNode(0)
        dummy.next = head


        prev_tail = dummy
        curr = head
        
        for _ in range(total_groups):
            tail = curr
            prev = None
            iteration = 0
            while iteration != k:
                iteration += 1
                nextUp = curr.next
                curr.next = prev
                prev = curr
                curr = nextUp
            tail.next = curr
            prev_tail.next = prev
            prev_tail = tail
        return dummy.next

        #   1 2 3
        #     p c n
        # 3 -> 2 -> 1 -> Null

# my thought is: 
#   define a function that finds the first k, then reverse
