class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    lands = [(row, col)]
                    grid[row][col] = 0
                    area = 1
                    while lands:
                        r_land, c_land = lands.pop()
                        candidates = [(r_land+r, c_land+c) for r, c in offsets if 0 <= r_land+r < len(grid)
                                      and 0 <= c_land+c < len(grid[0])]
                        lands.extend((r, c) for r, c in candidates if grid[r][c])
                        area += sum(grid[r][c] for r, c in candidates)
                        for r, c in candidates:
                            grid[r][c] = 0
                    max_area = max(max_area, area)
        return max_area
