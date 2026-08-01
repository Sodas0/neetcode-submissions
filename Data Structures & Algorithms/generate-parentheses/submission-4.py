class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def dfs(path, left_count, right_count):
            if len(path) == (2*n):
                out.append(path)

            if n - left_count >= 1:
                dfs(path+'(', left_count+1, right_count)
            
            if left_count - right_count > 0: # if more lefts than rights, can add a right
                dfs(path+')', left_count, right_count+1)
        
        dfs(path='', left_count=0, right_count=0)
        return out