# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            # case 1: both p and q are none
            if (not p and not q):
                return True # both none = same nodes = True
            
            # case 2: one of them is none and other is not, disqualify
            if (not p and q) or (not q and p):
                return False
            
            # case 3: their actual values differ
            if (p.val != q.val):
                return False
            
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        return dfs(p,q)