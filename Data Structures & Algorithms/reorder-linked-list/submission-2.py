# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #  0 1 2 3    6 5 4 
        #             p   
        # 2 4 6 8
        #     s. f
        #  0 6 1 5 2 4 3
        #  0 1 2 3 merge 6 5 4
        #  find middle, split list1&2
        #  reverse list2
        #  merge it back
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None

        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        curr = head
        curr2 = prev

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2