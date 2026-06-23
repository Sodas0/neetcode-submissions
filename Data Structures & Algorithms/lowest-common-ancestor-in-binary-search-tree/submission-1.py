# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node): # bad function name -- implies bool
            if not node:
                return node
            
            if (node.val == p.val) or (node.val == q.val):
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right: # guaranteed to be True iff left and right contain either p or q. (right must contain whichever p or q that left does not)
                return node
            
            return left or right # handles 3 cases at once
        
        return dfs(root)
            