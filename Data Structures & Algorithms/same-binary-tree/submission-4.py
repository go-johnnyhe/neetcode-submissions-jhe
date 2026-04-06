# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # dfs, if any value is different, return false
        def dfs(curr1, curr2):
            if not curr1 and not curr2:
                return True
            if not curr1 or not curr2 or curr1.val != curr2.val:
                return False
            return (dfs(curr1.left, curr2.left) and dfs(curr1.right, curr2.right))
        return dfs(p,q)