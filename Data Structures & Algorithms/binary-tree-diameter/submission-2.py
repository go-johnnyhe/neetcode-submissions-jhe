# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs to traverse all the nodes
        # on each node, res = left + right
        # keep the maximum
        maxRes = 0
        def dfs(curr):
            if not curr:
                return 0
            # bottom up since we need height
            left = dfs(curr.left)
            right = dfs(curr.right)
            # get current diameter
            diameter = left + right
            # update diameter
            nonlocal maxRes
            maxRes = max(diameter, maxRes)
            # return max height
            return 1 + max(left, right)
        dfs(root)
        return maxRes