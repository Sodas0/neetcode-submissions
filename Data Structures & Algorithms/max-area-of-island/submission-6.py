class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            if grid[r][c] != 1:
                return 0

            # mark visited
            grid[r][c] = 0
            area = 1 # current cell counts

            # check for bounds before each dfs
            if r + 1 < rows and grid[r+1][c] == 1:
                area += dfs(r+1, c)
            
            if r - 1 >= 0 and grid[r-1][c] == 1:
                area += dfs(r-1, c)
            
            if c + 1 < cols and grid[r][c+1] == 1:
                area += dfs(r, c+1)
            
            if c - 1 >= 0 and grid[r][c-1] == 1:
                area += dfs(r, c-1)
            
            return area
        # driver code
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.max_area = max(self.max_area, dfs(r,c))


        return self.max_area
