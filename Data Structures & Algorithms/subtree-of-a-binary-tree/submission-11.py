# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.is_same = False

        def same_tree(p, q) -> bool:
            # trivial case
            if (not p and not q):
                return True
            
            if (not p and q) or (not q and p):
                return False
            
            if (p.val != q.val):
                return False
            
            return same_tree(p.left, q.left) and same_tree(p.right, q.right)
            
        def dfs(node):
            if not node or self.is_same:
                return

            if same_tree(node, subRoot):
                self.is_same = True
                
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.is_same