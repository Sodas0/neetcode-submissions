# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # not balanced if depth of left and right subtree of root differ by more than 1
        self.is_balanced = True
        def depth(root):
            if not root:
                return 0
            
            left = depth(root.left)
            right = depth(root.right)

            if abs(left-right) > 1:
                self.is_balanced = False

            return 1 + max(left, right)
        
        depth(root)
        return self.is_balanced
        
       
