# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # could do any ttraversal of p and if the same traversal on q yields the same nodes, they're the same tree
        def dfs(p, q):
            # trivial case, does not matter if nodes are none
            if (not p and not q):
                return True
            
            # case 2: if p and not q, also false
            if (not p and q) or (not q and p):
                return False
            
            # case 3: 
            if (p.val != q.val):
                return False
            
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        return dfs(p,q)
            
            

