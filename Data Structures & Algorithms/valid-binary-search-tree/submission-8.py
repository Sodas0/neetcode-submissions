# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, leftbound, rightbound):
            if not node:
                return True # null node is trivially a BST
            
            if not (leftbound < node.val < rightbound): # if only condition of BST breaks, we know it's not valid.
                return False
            
            return dfs(node.left, leftbound, node.val) and dfs(node.right, node.val, rightbound)
        
        return dfs(node=root, leftbound=float('-inf'), rightbound=float('inf'))