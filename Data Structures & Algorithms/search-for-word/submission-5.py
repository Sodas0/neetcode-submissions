class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r,c,i):
            # if we've reached the end of the word with all matches, return True
            if i == len(word):
                return True
            
            # bounds checking
            if r>=rows or r<0 or c>=cols or c<0:
                return False
            
            # check if cell has been visited
            if board[r][c] == '@': # '@' means cell is visited
                return False

            # check if letters don't match
            if board[r][c] != word[i]:
                return False
            
            # if here, we know that board[r][c] == word[i].
            # mark cell as visited
            board[r][c] = '@'
            found = (
                dfs(r+1,c,i+1) or
                dfs(r-1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r,c-1,i+1)
            )
            board[r][c] = word[i]
            return found
        
        # driver for dfs
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False



# (r+1,c)
# (r-1,c)
# (r,c+1)
# (r,c-1)