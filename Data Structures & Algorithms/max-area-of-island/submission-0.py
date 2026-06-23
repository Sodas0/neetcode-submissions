class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max = 0 # maximum area of island seen
        self.local_area = 0 # keep track of local island size
    
        def dfs(r,c):
            # boundary / water check
            if r>=len(grid) or r<0 or c>=len(grid[0]) or c<0 or grid[r][c] != 1:
                return 
            
            # island detected, increment local area and set island to 0 to avoid infinite recursion
            self.local_area += 1
            grid[r][c] = 0

            # neighbor expansion
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # the main control loop that iterates through the grid and is what calls the recursion once an island is detected.
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: # detected an island
                    self.local_area = 0 # reset local area to avoid overcounting
                    dfs(r,c)
                    self.max = max(self.max, self.local_area)
        
        return self.max
