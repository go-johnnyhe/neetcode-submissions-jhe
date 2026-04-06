# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # left and right subtree differ > 1
        # no root: return 0
        # max difference of left and right sub trees 
        res = True
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            if abs(left - right) > 1:
                nonlocal res
                res = False
            return 1 + max(left, right)
        dfs(root)
        return res
