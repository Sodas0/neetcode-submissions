# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diam = 0

        def dfs(root):
            if not root:
                return 0 # height (number of edges)
            
            left = dfs(root.left)
            right = dfs(root.right)

            # check if new max diameter can be made during this recursive call
            self.max_diam = max(self.max_diam, left+right) # left+right is the current diameter, so height of left+right

            # return current node's contribution to whatever max of left/right height is so parent can use the higher
            # value for potentially breaking the current max.
            return 1 + max(left, right) 
        dfs(root)
        return self.max_diam