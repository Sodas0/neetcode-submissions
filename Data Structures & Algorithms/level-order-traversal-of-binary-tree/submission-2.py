# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] # empty level = []
        
        q = deque([root]) # initially contains root of tree
        out = [] # list of level lists

        while q:
            level = []
            for _ in range(len(q)): # iterate through the len of current q
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            out.append(level)
        
        return out
                
            
