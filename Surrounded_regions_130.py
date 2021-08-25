class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        protected = set()
        steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
        row, col = 0, 0
        for step_row, step_col in steps:
            while 0 <= row+step_row <= m and 0 <= col+step_col <= n:
                if board[row][col] == 'O':
                    queue = {(row, col)}
                    while queue:
                        coord = queue.pop()
                        protected.add(coord)
                        coord_row, coord_col = coord
                        for move_row, move_col in steps:
                            new_coord_row = coord_row + move_row
                            new_coord_col = coord_col + move_col
                            new_coord = (new_coord_row, new_coord_col)
                            if 0 <= new_coord_row < m and 0 <= new_coord_col < n and \
                               board[new_coord_row][new_coord_col] == 'O' and \
                               new_coord not in protected and new_coord not in queue:
                                queue.add(new_coord)
                row += step_row
                col += step_col
            if row == m:
                row -= 1
            if col == n:
                col -= 1

        for row in range(m):
            for col in range(n):
                if (row, col) not in protected:
                    board[row][col] = 'X'

