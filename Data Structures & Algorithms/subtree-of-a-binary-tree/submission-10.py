# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.is_same = False
        def sameTree(p,q):
            if (not p and not q):
                return True
            
            if (not p and q) or (not q and p):
                return False
            
            if (p.val != q.val):
                return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        def dfs(root):
            if not root or self.is_same:
                return
            
            if sameTree(root, subRoot):
                self.is_same = True

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.is_same