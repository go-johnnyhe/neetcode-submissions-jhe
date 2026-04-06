# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            curr1, curr2 = stack.pop()
            if not curr1 and not curr2:
                continue
            if not curr1 or not curr2 or curr1.val != curr2.val:
                return False
            stack.append((curr1.right, curr2.right))
            stack.append((curr1.left, curr2.left))
        return True