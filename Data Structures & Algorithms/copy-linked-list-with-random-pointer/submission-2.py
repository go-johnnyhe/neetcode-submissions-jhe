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
        dictionary = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            dictionary[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = dictionary[curr]
            copy.next = dictionary[curr.next]
            copy.random = dictionary[curr.random]
            curr = curr.next
        return dictionary[head]