# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(leftVal, root, rightVal):
            if not root:
                return True
            if not (leftVal < root.val < rightVal):
                return False
            return isValid(leftVal, root.left, root.val) and isValid(root.val, root.right, rightVal)
        return isValid(float("-inf"), root, float("inf"))