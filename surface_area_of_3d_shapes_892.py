class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        surface = 0
        for row in grid:
            prev = 0
            for height in row:
                surface += abs(prev - height) + (1 if height else 0)
                prev = height
            surface += height

        for c in range(len(grid[0])):
            prev = 0
            for r in range(len(grid)):
                surface += abs(prev - grid[r][c]) + (1 if grid[r][c] else 0)
                prev = grid[r][c]
            surface += grid[r][c]
        return surface
