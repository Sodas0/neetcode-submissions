# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # for a given node, do its left and right subtrees contain p and q?
            # if yes, that node is LCA
        
        def dfs(node):
            if not node:
                return 
            
            if node is p or node is q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right: # both found something
                return node
            
            return left if left else right # bubble up whichever node we found
        
        return dfs(root)

            
            