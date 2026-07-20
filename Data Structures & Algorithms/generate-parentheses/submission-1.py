class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def dfs(path, numleft, numright):
            if len(path) == (2*n):
                out.append(path)
            else:
                if numleft<n:
                    dfs(path + '(', numleft+1, numright)
                if numleft - numright >= 1:
                    dfs(path + ')', numleft, numright+1)
                
        dfs(path='', numleft=0, numright=0)
        return out