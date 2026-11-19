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
            if left and right:
                return node # node is the LCA since we found both in left/right
            
            # if here's we either found 1 in left, or 1 in right, or None, both useful info to pass up.
            # can handle all 3 cases simply:
            return left if left else right
        return dfs(root)
