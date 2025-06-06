class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # it tells us an empty position is represented by a dot 
                    continue           # so if we see a dot lets just skip it
                # this if statement says, 
                # if the number we are at in the loop exists in the row set
                # or the number we are at in the loop exists in the col set
                # or exists in the current square also (3x3)
                # then its a duplicate
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[r//3, c//3]): # tells us the current square were in 
                    return False
                # if its still valid we need to update all three of our sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r // 3, c // 3].add(board[r][c]) 
        return True
