# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.is_same = False
        # define a function called same tree that takes in two nodes and determines if they contain the same tree.
        def same_tree(p,q):
            if not p and not q:
                return True

            if (not p and q) or (p and not q):
                return False

            if p.val != q.val:
                return False

            return same_tree(p.left, q.left) and same_tree(p.right, q.right)           

        # then, use the same tree function to recurse on root using subroot as the tree to compare against.
        def dfs(root, subRoot):
            if not root:
                return
            
            if same_tree(root, subRoot):
                self.is_same = True
            
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        dfs(root,subRoot)
        return self.is_same
        # the time complexity of this algorithm should be number of nodes in root -- M times number of nodes in subRoot -- N
        # so O(M*N)