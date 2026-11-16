# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxsofar):
            if not node:
                return 0
            good = 1 if node.val>=maxsofar else 0
            maxsofar = max(maxsofar, node.val)
            return good + dfs(node.left, maxsofar) + dfs(node.right, maxsofar)
        return dfs(root, maxsofar=float('-inf'))