# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mp_so_far = float('-inf')
        
        # left, root, right allows to to look at long paths.
        def dfs(node):
            if not node:
                return 0

            leftsum = max(dfs(node.left), 0)
            rightsum = max(dfs(node.right), 0)

            self.mp_so_far = max(self.mp_so_far, leftsum + node.val + rightsum)

            return node.val + max(leftsum, rightsum) # choose the child with highest maxpathsum for extending current path


        
        # call dfs on each node.
        # try first
        dfs(root)
        return self.mp_so_far
