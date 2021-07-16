class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [{i for i in range(n)} for _ in range(n)]
        return sum(self.analyze(n, board))
        
    def analyze(self, n, board, count=0):
        if count == n:
            yield 1
        else:
            for num in board[0]:
                new_board = []
                for i, row in enumerate(board[1:], 1):
                    new_board.append(row.copy())
                    new_board[-1] -= {num, num-i, num+i}
                yield from self.analyze(n, new_board, count+1)

