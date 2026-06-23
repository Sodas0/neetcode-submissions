class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # overall idea is to use a set to track duplicates across rows first, then columns, then 3x3 grids.
        # main notion is to reset the set across each pass through rows, columns, and 3x3 sections.

        # 1. validate each row (rows are easy, each row is just the entire sublist)
        for r in range(9): # fix rows
            seen = set()
            for c in range(9): 
                if board[r][c] == ".": # ignore empty squares
                    continue
                if board[r][c] not in seen: # first time seeing value
                    seen.add(board[r][c])
                else: return False # otherwise, it has been seen before, so duplicate detected!!
                    
        # 2. validate each column (columns are slightly more tricky.)    
        # iterate through cols:
        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] == ".": #ignore
                    continue
                if board[r][c] not in seen:
                    seen.add(board[r][c])
                else: return False
        
        # 3. validate each 3x3 grid (trickiest one to iterate, idea is to iterate through)
        # step by 3 in rows and cols in outer loops to identify 1 grid.
        for box_row in range(0,9,3): 
            for box_col in range(0,9,3):
                seen = set()
                for r in range(box_row, box_row+3):
                    for c in range(box_col, box_col+3):
                        if board[r][c] == ".": #ignore
                            continue
                        if board[r][c] not in seen:
                            seen.add(board[r][c])
                        else: return False
        return True







                