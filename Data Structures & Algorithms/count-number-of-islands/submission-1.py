class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols: # bounds check
                return 
            
            if grid[r][c] == '0':
                return # we don't care if its 0
            
            # if here, grid[r][c] == 1
            # mark it as visited (set to 0)
            grid[r][c] = '0'
            
            # 4-neighbor recursion
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        # driver
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r,c)
        return islands
