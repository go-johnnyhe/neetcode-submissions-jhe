# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(curr1, curr2):
            if not curr1 and not curr2:
                return True
            if not curr1 or not curr2 or curr1.val != curr2.val:
                return False
            return (isSame(curr1.left, curr2.left) and isSame(curr1.right, curr2.right))
        if not root:
            return False
        if isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)