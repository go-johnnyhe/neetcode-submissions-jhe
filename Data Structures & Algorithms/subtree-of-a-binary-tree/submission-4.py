# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if current is the same tree
        # keep exploring left & right
        def isSame(p, q):
            if not p and not q:
                return True
            if (not p and q) or (not q and p) or (p.val != q.val):
                return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        if not root and subRoot:
            return False
        if not subRoot:
            return True
        return (isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))


