# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1 = ""
        curr1 = l1
        while curr1:
            nums1 = str(curr1.val) + nums1
            curr1 = curr1.next
        nums2 = ""
        curr2 = l2
        while curr2:
            nums2 = str(curr2.val) + nums2
            curr2 = curr2.next

        sum_nums = str(int(nums1) + int(nums2))
        dummy = ListNode(0)
        curr = dummy
        for num in reversed(sum_nums):
            curr.next = ListNode(int(num))
            curr = curr.next
        return dummy.next