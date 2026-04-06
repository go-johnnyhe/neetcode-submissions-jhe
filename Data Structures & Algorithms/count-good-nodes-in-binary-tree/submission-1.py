# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # count non-decreasing paths
        # dfs
        count = 0
        def dfs(curr, prevVal):
            nonlocal count
            if not curr:
                return
            if curr.val >= prevVal:
                count += 1
            dfs(curr.left, max(prevVal, curr.val))
            dfs(curr.right, max(prevVal, curr.val))
        dfs(root, float("-inf"))
        return count
