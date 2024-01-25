class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in grid:
            if not row[0]:
                for i in range(len(row)):
                    row[i] = not row[i]

        min_ones = ceil(len(grid) / 2)
        for col in range(1, len(grid[0])):
            if sum(grid[row][col] for row in range(len(grid))) < min_ones:
                for row in range(len(grid)):
                    grid[row][col] = not grid[row][col]

        total = 0
        for row in grid:
            temp = 0
            for bit in row:
                temp = temp * 2 + bit
            total += temp
        return total
