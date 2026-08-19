class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # this is multi source bfs where we find each cell of interest and do bfs outwards from each cell at the same time
        # we update grid to be the distance FROM each treasure cell outwards and then mark them as visited so they don't
        # get re-updated with a worse weight.
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def updateDist(r, c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return
            if (r,c) in visited or grid[r][c] == -1:
                return
            
            visited.add((r,c))
            q.append([r,c])
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append([r,c])
    
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                # 4 way bfs
                updateDist(r+1,c)
                updateDist(r-1,c)
                updateDist(r,c+1)
                updateDist(r,c-1)
            dist += 1
        
