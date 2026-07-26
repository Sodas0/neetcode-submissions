# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.is_same = False

        def same_tree(p, q):
            if (not p and not q):
                return True
            
            if (not p and q) or (not q and p):
                return False
            
            if (p.val != q.val):
                return False
            
            return same_tree(p.left, q.left) and same_tree(p.right, q.right)

        # then check every node to see if it contains subroot
        def dfs(root):
            if not root:
                return
            
            if same_tree(root, subRoot):
                self.is_same = True
            
            return dfs(root.left) or dfs(root.right)
        
        dfs(root)
        return self.is_same
            
        