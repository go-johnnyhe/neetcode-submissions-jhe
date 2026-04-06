# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        # if non decreasing path: good node
        # dfs to track curr node and prevVal
        # if curr > prevVal, count += 1
        def dfs(curr, prevVal):
            if not curr:
                return
            if curr.val >= prevVal:
                res[0] += 1
            dfs(curr.left, max(curr.val, prevVal))
            dfs(curr.right, max(curr.val, prevVal))
        dfs(root, float('-inf'))
        return res[0]
            