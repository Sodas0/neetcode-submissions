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
            if (node is p or node is q):
                return node
            
            left, right = dfs(node.left), dfs(node.right)

            if left and right:
                return node # means that we found both in left and right, so current must be lca
            # otherwise, we want to pass left if we found left, otherwise, right if we pass right, or None.
            return left if left else right # handles all 3 cases.
        return dfs(root)