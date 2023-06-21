class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def neighber(r, c):
            rows = [row for row in [r-1, r, r+1] if 0<=row<len(board)]
            cols = [col for col in [c-1, c, c+1] if 0<=col<len(board[0])]
            neighbers = [(row, col) for row in rows for col in cols if (row, col) != (r, c)]
            return sum(board[r][c] for r, c in neighbers)

        flips = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                n = neighber(row, col)
                if (board[row][col] and (n < 2 or n > 3)) or (not board[row][col] and n == 3):
                    flips.append((row, col))
        for row, col in flips:
            board[row][col] = 0 if board[row][col] else 1
