class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        self.local_area = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            # boilerplate
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            
            if grid[r][c] != 1:
                return # we really only care about 1s
            
            # internalize that once we're here, grid[r][c] is 1.
            self.local_area += 1
            grid[r][c] = 0 # mark visited then recurse 4 way

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # driver code
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.local_area = 0       
                    dfs(r,c)
                    self.max_area = max(self.max_area, self.local_area)
        return self.max_area
            