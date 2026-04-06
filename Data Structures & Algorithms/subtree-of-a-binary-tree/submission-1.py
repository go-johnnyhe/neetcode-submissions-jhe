# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # for each node, examine if the subroot matches
        # => starting from each node of the root, see if subroot
        # is an EXACT match, O(n^2)
        # bad examples:
        #   root is too long
        #   subroot is too long
        #   one of the values doesn't match
        # two recursions: 1. each node
        #                 2. compare each to subroot
        def isSameTree(curr1, curr2):
            if not curr1 and not curr2:
                return True
            if not curr2 or not curr1:
                return False
            if curr1.val != curr2.val:
                return False
            return isSameTree(curr1.left, curr2.left) and isSameTree(curr1.right, curr2.right)
        if not root and not subRoot:
            return True
        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)