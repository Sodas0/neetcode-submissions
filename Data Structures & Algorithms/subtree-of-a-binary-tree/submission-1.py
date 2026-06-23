# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.is_same = False

        # define a function same_tree that checks whether two roots contain identical trees.
        def same_tree(p,q):
            if (not p and not q):
                return True
            
            if (not p and q) or (p and not q):
                return False
            
            if (p.val != q.val):
                return False
            
            return same_tree(p.left, q.left) and same_tree(p.right, q.right)
        
        # now we want check eery node in root to see if it contains subroot. 
        def dfs(root):
            if not root:
                return
            
            if same_tree(root, subRoot):
                self.is_same = True
            
            return dfs(root.left) or dfs(root.right)
    
        dfs(root)
        return self.is_same