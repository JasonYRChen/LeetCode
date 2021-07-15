class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [{i for i in range(n)} for _ in range(n)]
        solutions = []
        for result in self.dfs(n, board, []):
            solution = []
            for idx in result:
                row = ['.'] * n
                row[idx] = 'Q'
                solution.append(''.join(row))
            solutions.append(solution)
        return solutions

    def dfs(self, n, board, result):
        if not board:
            yield result
        else:
            for num in board[0]:
                new_board = []
                result.append(num)
                for i in range(1, len(board)):
                    temp = board[i].copy()
                    if num in temp:
                        temp.remove(num)
                    if num + i in temp:
                        temp.remove(num + i)
                    if num - i in temp:
                        temp.remove(num - i)
                    new_board.append(temp)
                yield from self.dfs(n, new_board, result)
                result.pop()

