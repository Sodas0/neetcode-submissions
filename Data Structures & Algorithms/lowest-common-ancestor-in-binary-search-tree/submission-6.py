# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if both left and right contain p / q; current node is LCA.
        def dfs(node):
            if not node:
                return

            if node is p or node is q: # 
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node # found both separately.

            return left if left else right # whichever finds something
        
        return dfs(root)