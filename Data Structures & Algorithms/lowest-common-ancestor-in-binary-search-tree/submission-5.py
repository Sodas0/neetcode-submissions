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
            
            left, right = dfs(node.left), dfs(node.right)

            if left and right: # both found p and q separately
                return node
            
            return left if left else right # return whichever found something
        
        return dfs(root)