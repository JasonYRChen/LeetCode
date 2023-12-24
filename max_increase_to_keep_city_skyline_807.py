class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [max(row) for row in grid]
        col_max = [max(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]
        increment = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                increment += min(row_max[r], col_max[c]) - grid[r][c]
        return increment
