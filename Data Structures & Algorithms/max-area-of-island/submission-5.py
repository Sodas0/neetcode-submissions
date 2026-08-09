class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            # bounds check
            if r<0 or r>=rows or c<0 or c>=cols:
                return 0 
            
            if grid[r][c] != 1:
                return 0
            
            # if here, then grid[r][c] is for sure 1
            # mark visited
            grid[r][c] = 0
            
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        
        # driver code
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.local_area = 0
                    self.max_area = max(self.max_area, dfs(r,c))

        return self.max_area
