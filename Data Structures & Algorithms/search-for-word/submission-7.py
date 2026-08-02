class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r,c,i):
            # early true return
            if i == len(word):
                return True
            
            # bounds checking
            if r<0 or r>=rows or c<0 or c>=cols:
                return False
            
            # if already visited
            if board[r][c] == '@':
                return False

            # actual character match
            if board[r][c] != word[i]:
                return False
            
            # here if board[r][c] unvisited and matches word[i]
            # mark as visited before doing anything
            board[r][c] = '@'
            # 4 way dfs
            found = (
                dfs(r+1,c,i+1) or
                dfs(r-1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r,c-1,i+1)
            )
            board[r][c] = word[i]
            return found

        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
            

            
