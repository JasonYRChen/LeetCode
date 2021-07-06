class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s_col, s_row, s_block = set(), set(), set()
            div_block, mod_block = divmod(i, 3)
            for j in range(9):
                # row first
                if board[i][j].isdigit() and board[i][j] not in s_row:
                    s_row.add(board[i][j])
                elif board[i][j] != '.':
                    return False
                
                # col first
                if board[j][i].isdigit() and board[j][i] not in s_col:
                    s_col.add(board[j][i])
                elif board[j][i] != '.':
                    return False
                
                # block
                div_e, mod_e = divmod(j, 3)
                r = mod_block * 3 + div_e
                c = div_block * 3 + mod_e
                if board[r][c].isdigit() and board[r][c] not in s_block:
                    s_block.add(board[r][c])
                elif board[r][c] != '.':
                    return False
        return True
