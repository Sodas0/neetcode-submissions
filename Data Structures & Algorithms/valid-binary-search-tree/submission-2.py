# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # problem is about intervals. 
        def valid(node, left_bound, right_bound):
            if not node:
                return True # Null node is still a valid bst
            if not (node.val < right_bound and node.val > left_bound):
                return False # bst condition breaks 
            
            # first valid() updates right bounds and second one updates left bound.
            return (
                    valid(node.left, left_bound, node.val) and 
                    valid(node.right, node.val, right_bound)
                    )
            
        return valid(node=root, left_bound=float('-inf'), right_bound=float('inf'))

            
            
            
            