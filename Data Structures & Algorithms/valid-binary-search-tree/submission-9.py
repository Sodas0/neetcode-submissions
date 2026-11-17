# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid = True
        def dfs(node, leftbound, rightbound):
            if not node:
                return 
            if not (leftbound < node.val < rightbound):
                self.is_valid = False
            
            dfs(node.left, leftbound, node.val)
            dfs(node.right, node.val, rightbound)

        dfs(root, leftbound=float('-inf'), rightbound=float('inf'))
        return self.is_valid