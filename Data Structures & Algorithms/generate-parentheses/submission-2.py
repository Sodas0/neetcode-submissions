class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def dfs(path, count_left, count_right):
            if len(path) == (2*n):
                out.append(path)
            else:
                if count_left < n: # can add '('
                    dfs(path+'(', count_left+1, count_right)
                if count_left - count_right >= 1: 
                    dfs(path+')', count_left, count_right+1)

        dfs(path='', count_left=0, count_right=0)
        return out