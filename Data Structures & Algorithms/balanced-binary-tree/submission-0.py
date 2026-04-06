# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr:
                return 0, True
            l_height, l_balanced = dfs(curr.left)
            r_height, r_balanced = dfs(curr.right)
            balanced = False
            if l_balanced and r_balanced and abs(l_height - r_height) <=1:
                balanced = True
            return 1 + max(l_height, r_height), balanced
        height, balanced = dfs(root)
        return balanced