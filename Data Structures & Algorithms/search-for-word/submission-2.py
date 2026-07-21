class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r,c,i):
            # check if index matches length of word to see if we're done
            if i == len(word):
                return True
            
            # guardrails for grid search
            if r<0 or r>=rows or c<0 or c>=cols:
                return False
            
            # check if visited 
            if board[r][c] == '@':
                return False
            
            # check if letter doesn't match
            if board[r][c] != word[i]:
                return False
            
            # processing stage:
            # mark as visited before anything
            board[r][c] = '@'
            found = ( 
                dfs(r+1,c,i+1) or 
                dfs(r-1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r,c-1,i+1)
            ) # grid search
            board[r][c] = word[i] # restore
            return found
        
        # driver
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
