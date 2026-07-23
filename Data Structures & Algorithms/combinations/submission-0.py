class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # k numbers from range [1,n].  (1..n) = 1 indexed.
        out = []

        def dfs(path, start):
            if len(path) == k:
                out.append(path.copy())
                return
            
            for i in range(start, n+1):                
                path.append(i) # i represents different values from 1..n inc.
                dfs(path, i+1)
                path.pop()
        
        dfs(path=[], start=1)
        return out