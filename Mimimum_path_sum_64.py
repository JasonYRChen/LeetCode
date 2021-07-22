class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Dynamic programming. Time: O(mn), space: O(n)
        g = [0] + [float('inf')] * (len(grid[0]) - 1)
        for row in range(len(grid)):
            g[0] += grid[row][0]
            for col in range(1, len(grid[0])):
                g[col] = min(g[col-1], g[col]) + grid[row][col]
        return g[-1]

