class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # the idea is we can use bitwise to masking a variable that duplicate in that row or col or squares
        rows = [0]*9
        cols = [0]*9
        squares = [0]*9

        for r in range(9):
            for c in range(9):
                # we can skip a dot, sine we don't need to care that value 
                if board[r][c] == ".":
                    continue
                
                val=int(board[r][c])-1
                # do a masking if the value is already exits it will return true
                if (1 << val ) & rows[r]:
                    return False
                # same logic as row but chagne to col
                if (1 << val ) & cols[c]:
                    return False
                # also same logic as col but instread go to squares
                if (1 << val ) & squares[(r//3)*3 + (c // 3)]:
                    return False
                
                # if we no found at r,c move to next r,c 
                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[(r//3)*3 + (c // 3)] |= (1 << val)
        
        return True