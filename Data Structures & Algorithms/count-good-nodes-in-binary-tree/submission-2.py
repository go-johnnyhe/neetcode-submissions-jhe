# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(curr, prevVal):
            if not curr:
                return
            if curr.val >= prevVal:
                nonlocal count
                count += 1
            dfs(curr.left, max(curr.val, prevVal))
            dfs(curr.right, max(curr.val, prevVal))
        dfs(root, float('-inf'))
        return count