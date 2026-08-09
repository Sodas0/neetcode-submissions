class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            # bounds check
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            
            # check if not 1 (we dont care if grid[r][c] is a 0)
            if grid[r][c] != '1':
                return
            
            # here if grid[r][c] is 1.
            # mark as visited:
            grid[r][c] = '0'
            

            # 4-neighbor recursion
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        # driver
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count+=1
                    dfs(r,c)
        
        return count
