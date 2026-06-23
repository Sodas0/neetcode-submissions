# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        initial_min, initial_max = -1001, 1001
        # each subtree's root must satisfy the condition: 
        def dfs(node, min_val, max_val):
            if not node:
                return True # trivial case
            
            if not (min_val < node.val < max_val):
                return False # breaks condition
            
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        return dfs(root, initial_min, initial_max)