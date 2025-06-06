class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        pawns = 0
        for row in range(8):
            for col in range(8):
                if board[row][col] == 'R':
                    r, c = row, col

        for y in range(r-1, -1, -1):
            if board[y][c] != '.':
                if board[y][c] == 'p':
                    pawns += 1
                break
        for y in range(r+1, 8):
            if board[y][c] != '.':
                if board[y][c] == 'p':
                    pawns += 1
                break
        for x in range(c-1, -1, -1):
            if board[r][x] != '.':
                if board[r][x] == 'p':
                    pawns += 1
                break
        for x in range(c+1, 8):
            if board[r][x] != '.':
                if board[r][x] == 'p':
                    pawns += 1
                break

        return pawns
