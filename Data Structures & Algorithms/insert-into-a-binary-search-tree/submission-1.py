# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # i think that BST insertions can only be at leaves.
        def dfs(node):
            if not node:
                # we will have recursed top-down until we reach a leaf node, and the first leaf node is where we insert.
                return TreeNode(val)
                
            # two cases: val is either lower or higher than current node.
            # recurse left
            if val < node.val:
                node.left = dfs(node.left)
            
            #recurse right
            elif val > node.val:
                node.right = dfs(node.right)
            
            return node
        
        return dfs(root)
