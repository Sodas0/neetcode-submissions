# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return
            
            if node is p or node is q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node # found both
            # handles case where found 1 (either left or right)or found none. (right defaults to none if not found).
            return left if left else right 
        return dfs(node=root)
