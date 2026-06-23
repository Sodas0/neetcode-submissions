class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        # we need a control loop that iterates through the graphs and recurses into a '1' if detected.

        # we also need a dfs that handles the recursion for the control loop.


        def dfs(r,c):
            # data validation:
            if r>=len(grid) or r<0 or c>=len(grid[0]) or c<0 or grid[r][c] == '0':
                return
            
            grid[r][c] = '0' # avoids infinite recursion    

            # recurse into it in all 4 directions.
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        # main control loop:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r,c)
                
        return count
            
        

