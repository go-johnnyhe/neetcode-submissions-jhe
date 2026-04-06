# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def findMax(curr):
            if not curr:
                return 0
            leftMax = max(findMax(curr.left), 0)
            rightMax = max(findMax(curr.right), 0)
            res[0] = max(res[0], curr.val + leftMax + rightMax)
            return curr.val + max(leftMax, rightMax)
        findMax(root)
        return res[0]