# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = 0
        def dfs(curr):
            if not curr:
                return 0
            dfs(curr.left)
            self.count += 1
            if self.count == k:
                self.res = curr.val
            dfs(curr.right)
        dfs(root)
        return self.res