# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # We are essentially trying to answer the question "Do my left and right subtrees contain either p or q?" 
        # we know that if left contains either p or q and right also contains either p or q -- that node itself must be the LCA.
        # However, how can we handle the case where the node itself is either p or q --- recursion !
        
        def dfs(node):
            if not node:
                return node
            
            if (node.val == p.val) or (node.val == q.val):
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            # now we are assuming (hopefully correctly) that left and right contain each contain p or q.
            if left and right: # Guaranteed to be True iff our dfs found that left and right each contain p or q.
                return node
            
            return left or right 
        
        return dfs(root)

            