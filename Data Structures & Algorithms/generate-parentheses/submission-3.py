class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        # essenially generting different permutations of pairs?
        def dfs(path, left_count, right_count):
            if len(path) == (2*n):
                out.append(path)
            
            if left_count < n: # can add a left parenthesis
                dfs(path+'(', left_count+1, right_count)
            
            if left_count - right_count >= 1: # difference of at least 1 means there's an unmatched left, so we can add a right
                dfs(path+')', left_count, right_count+1)
            
            # note: don't need to explicitly do path.append or path.pop since strings immutable and we get
            #       backtracking for 'free' because of it.

        dfs(path='', left_count=0, right_count=0)
        return out