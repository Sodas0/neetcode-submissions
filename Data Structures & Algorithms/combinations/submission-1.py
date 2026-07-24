class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # output contains lists of k numbers each with values ranging from [1..n] (one indexed)
        out = []

        def dfs(start, path):
            if len(path) == k:
                out.append(path.copy())
            
            for i in range(start, n+1): #since we want to include n.
                path.append(i)
                dfs(i+1, path)
                path.pop()
        
        dfs(start=1, path=[]) #starting at 1 since one indexed.
        return out