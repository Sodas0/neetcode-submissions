# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level order traversal is just bfs but print that shi lol
        if not root:
            return []
        lvl_order = []
        q = deque([root])

        while q:
            curr_lvl = []
            for _ in range(len(q)):
                # fifo; popleft in q to expand node
                node = q.popleft()
                curr_lvl.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl_order.append(curr_lvl)
        
        return lvl_order