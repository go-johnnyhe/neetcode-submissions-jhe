"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        listHolder = {}
        while curr:
            listHolder[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            listHolder[curr].next = listHolder.get(curr.next)
            listHolder[curr].random = listHolder.get(curr.random)
            curr = curr.next
        return listHolder[head]

        # uhh I feel the logic is to loop through the linkedlist twice,
        # first time establish the new linkedlist's val and next,
        # second time link the random nodes together