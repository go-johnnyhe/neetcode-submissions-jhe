# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base: at the end, return 0
        # at a given node, just return the max of (left, right) + 1
        def getMaxDepth(node):
            if not node:
                return 0
            return max(getMaxDepth(node.left), getMaxDepth(node.right)) + 1
        return getMaxDepth(root)