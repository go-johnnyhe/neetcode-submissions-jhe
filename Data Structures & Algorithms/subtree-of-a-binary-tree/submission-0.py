# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(curr, subCurr):
            if not curr and not subCurr:
                return True
            if curr and subCurr and curr.val == subCurr.val:
                return (dfs(curr.left, subCurr.left)
                and dfs(curr.right, subCurr.right))
            return False
        if not subRoot:
            return True
        if not root:
            return False
        if dfs(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)